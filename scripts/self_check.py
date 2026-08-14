#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFERENCES = ROOT / "references"

REQUIRED_REFERENCES = [
    "00-current-overrides.md",
    "01-evidence-and-version-routing.md",
    "02-director-workflow.md",
    "03-reference-assets-and-identity.md",
    "04-time-space-continuity.md",
    "05-action-physics-and-performance.md",
    "06-camera-pov-and-composition.md",
    "07-long-takes-transitions-and-continuation.md",
    "08-light-environment-effects-and-sound.md",
    "09-specialized-scenes.md",
    "10-prompt-templates.md",
    "11-qa-diagnosis-and-ab.md",
    "12-rule-status-and-sources.md",
    "13-jin-ip-and-audio-rules.md",
]

LEGACY_REFERENCES = {
    "director-methodology.md",
    "jin-project-rules.md",
    "prompt-templates.md",
    "qa-and-diagnosis.md",
}

REQUIRED_TEXT = {
    "00-current-overrides.md": [
        "【反向约束与失败保险】",
        "如果用户说“通过”",
        "Sera：不得说词或句子",
        "约 9–12 个可执行、可见的动作或状态节点",
    ],
    "01-evidence-and-version-routing.md": [
        "官方能力不能被简化",
        "项目工作假设",
        "需要即时核验的事项",
    ],
    "03-reference-assets-and-identity.md": [
        "没有素材标签时使用全程一致的普通角色名",
    ],
    "10-prompt-templates.md": [
        "不虚构素材引用",
        "如需第二次遮挡",
    ],
    "11-qa-diagnosis-and-ab.md": [
        "一次只改一个主变量",
        "十维成片验收",
    ],
    "13-jin-ip-and-audio-rules.md": [
        '音频：{角色} "声音或台词"（语气方向）',
        "Sera 不得说词或句子",
        "默认不新增 Sera 音频行",
        "默认不新增糯糯音频行",
        "咕咕嘎嘎！",
        "菲比啾比",
    ],
}

REQUIRED_HEADINGS = {
    "00-current-overrides.md": [
        "当前硬规则",
        "30 秒动作密度",
        "第一人称与镜头过渡",
        "已通过版本保护",
        "角色声音硬护栏",
    ],
    "01-evidence-and-version-routing.md": [
        "证据等级",
        "官方能力与生产默认值",
        "版本选择矩阵",
        "时长与动作密度",
        "需要即时核验的事项",
    ],
    "02-director-workflow.md": [
        "制作简报",
        "专家独立提案",
        "六步融合",
        "冲突裁决",
        "状态模型",
    ],
    "03-reference-assets-and-identity.md": [
        "素材职责卡",
        "统一人物锚点",
        "视频参考拆分",
        "素材优先级",
    ],
    "04-time-space-continuity.md": [
        "C1／C2／C3 检查点",
        "人物路线与摄影机路线",
        "遮挡期间的状态",
        "续写与真实尾帧",
    ],
    "05-action-physics-and-performance.md": [
        "动作因果链",
        "起因—过程—结果",
        "转身",
        "技能动作",
        "多角色互动",
    ],
    "06-camera-pov-and-composition.md": [
        "摄影机任务",
        "景别变化",
        "第一人称稳定观察",
        "前中后景与视差",
    ],
    "07-long-takes-transitions-and-continuation.md": [
        "何时使用长镜头",
        "视觉接力媒介",
        "遮挡转场",
        "五空间高速穿越",
        "续写工作流",
    ],
    "08-light-environment-effects-and-sound.md": [
        "动态光影公式",
        "环境作为物理证据",
        "特效因果",
        "台词与拟声格式",
        "动态声场",
    ],
    "09-specialized-scenes.md": [
        "30 秒高密度编排",
        "战斗与技能",
        "奔跑与追逐",
        "微表情与矛盾情绪",
        "现实空间 Q 角色",
    ],
    "11-qa-diagnosis-and-ab.md": [
        "生成前硬门禁",
        "十维成片验收",
        "常见故障矩阵",
        "最小改动协议",
        "A/B 测试",
    ],
    "12-rule-status-and-sources.md": [
        "旧规则状态表",
        "新旧经验冲突的裁决",
        "当前来源索引",
        "更新边界",
    ],
    "13-jin-ip-and-audio-rules.md": [
        "当前音频格式",
        "角色权限",
        "旧规则冲突",
        "音频自检",
    ],
}

FINAL_TEMPLATE_HEADINGS = [
    "2.0 短镜头",
    "2.5 15–30 秒",
    "2.5 30 秒高密度",
    "图生视频",
    "首尾帧",
    "延长／续写",
    "长镜头",
    "战斗／技能",
    "奔跑追逐",
    "微表情",
    "POV 与 Q 角色",
    "产品／OOTD",
]

BANNED_IN_ACTIVE_FILES = [
    r"Seedance\s*2\.0\s*只能",
    r"2\.0\s*只能做",
    r"长镜头一定比分镜稳定(?!.*作废)",
    r"负面约束越多越安全(?!.*作废)",
    r"第一人称因可爱产生微震(?!.*废弃)",
    r"MMDiT.*已确认官方架构(?!.*撤回)",
    r"RayFlow.*已确认官方架构(?!.*撤回)",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_frontmatter(errors: list[str], text: str) -> None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        fail(errors, "SKILL.md 缺少有效 YAML frontmatter")
        return
    keys = []
    for line in match.group(1).splitlines():
        if line and not line.startswith((" ", "\t")) and ":" in line:
            keys.append(line.split(":", 1)[0].strip())
    if set(keys) != {"name", "description"}:
        fail(errors, f"SKILL.md frontmatter 只能包含 name 和 description，当前为 {keys}")
    if "name: jin-seedance-director" not in match.group(1):
        fail(errors, "SKILL.md name 不正确")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not SKILL.exists():
        print("FAIL: SKILL.md 不存在")
        return 1

    skill_text = SKILL.read_text(encoding="utf-8")
    check_frontmatter(errors, skill_text)

    skill_lines = skill_text.splitlines()
    if len(skill_lines) > 500:
        fail(errors, f"SKILL.md 超过 500 行：{len(skill_lines)}")

    for name in REQUIRED_REFERENCES:
        path = REFERENCES / name
        if not path.exists():
            fail(errors, f"缺少参考文件：{name}")
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not text.startswith("# "):
            fail(errors, f"{name} 缺少一级标题")
        if len(lines) > 100 and "## 目录" not in text:
            fail(errors, f"{name} 超过 100 行但缺少目录")
        if re.search(r"\b(TODO|TBD|FIXME)\b", text, flags=re.I):
            fail(errors, f"{name} 含未完成标记")
        if f"references/{name}" not in skill_text:
            fail(errors, f"SKILL.md 未路由到 {name}")

    for legacy in LEGACY_REFERENCES:
        if (REFERENCES / legacy).exists():
            fail(errors, f"旧参考文件仍存在，可能产生冲突：{legacy}")

    linked = re.findall(r"\]\((references/[^)#]+\.md)\)", skill_text)
    for rel in linked:
        if not (ROOT / rel).exists():
            fail(errors, f"SKILL.md 链接不存在：{rel}")

    for name, phrases in REQUIRED_TEXT.items():
        path = REFERENCES / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                fail(errors, f"{name} 缺少关键规则：{phrase}")

    for name, headings in REQUIRED_HEADINGS.items():
        path = REFERENCES / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if f"## {heading}" not in text:
                fail(errors, f"{name} 缺少关键分区：{heading}")

    template_path = REFERENCES / "10-prompt-templates.md"
    if template_path.exists():
        template_text = template_path.read_text(encoding="utf-8")
        for heading in FINAL_TEMPLATE_HEADINGS:
            match = re.search(
                rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)",
                template_text,
                flags=re.M | re.S,
            )
            if not match:
                fail(errors, f"模板库缺少最终模板：{heading}")
            elif "【反向约束与失败保险】" not in match.group(1):
                fail(errors, f"模板未以失败保险收尾：{heading}")

    active_files = [SKILL] + [
        REFERENCES / name for name in REQUIRED_REFERENCES if name != "12-rule-status-and-sources.md"
    ]
    for path in active_files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in BANNED_IN_ACTIVE_FILES:
            if re.search(pattern, text):
                fail(errors, f"{path.name} 含过度绝对化旧规则：{pattern}")

    all_text = "\n".join(
        p.read_text(encoding="utf-8")
        for p in [SKILL] + [REFERENCES / n for n in REQUIRED_REFERENCES]
        if p.exists()
    )
    if "【反向约束与失败保险】" not in all_text:
        fail(errors, "全库缺少【反向约束与失败保险】")
    if "用户说“通过”" not in all_text:
        fail(errors, "全库缺少通过版本保护")
    if re.search(r'音频：\{Sera\}\s*"[^"]*[A-Za-z\u4e00-\u9fff][^"]*"', all_text):
        fail(errors, "检测到 Sera 的词汇性台词示例")

    md_files = sorted(REFERENCES.glob("*.md"))
    unlinked = [p.name for p in md_files if f"references/{p.name}" not in skill_text]
    if unlinked:
        warnings.append("存在未由 SKILL.md 路由的参考文件：" + ", ".join(unlinked))

    if errors:
        print("SELF-CHECK FAILED")
        for item in errors:
            print(f"- ERROR: {item}")
        for item in warnings:
            print(f"- WARNING: {item}")
        return 1

    print("SELF-CHECK PASSED")
    print(f"- SKILL.md: {len(skill_lines)} lines")
    print(f"- Reference zones: {len(REQUIRED_REFERENCES)}")
    print(f"- Reference markdown files: {len(md_files)}")
    print("- Frontmatter, links, section TOCs, key rules, legacy conflicts, and role-audio guards passed")
    for item in warnings:
        print(f"- WARNING: {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
