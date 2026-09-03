---
name: jin-video-director-flow
description: Build, revise, and study AI video prompts through a process-first director workflow. Use when turning an idea, image reference, video reference, or emotional beat into a duration-aware shot sequence; when defining terminology and reference responsibilities; when writing explicit shot content, camera position, foreground/midground/background staging, micro-performance, sound, and predicted failure guards; or when extracting reusable prompt methods from paired original prompts and generated videos.
---

# JIN Video Director Flow

把创作意图转换为可按顺序执行的镜头流程。保持本 Skill 简短；用模板教会使用者每个格子负责什么，不把理论堆进最终提示词。

## 工作优先级

按以下职责理解各部分：

1. **镜头内容**决定画面中发生什么以及摄影机怎样看见它。
2. **表演要求**决定角色怎样用可见动作完成镜头内容。
3. **术语解释、视觉风格和参考图说明**负责搭建人物、物体与场景。
4. **声音**在画面确定后补充。
5. **禁止**只拦截本次任务最可能发生的崩溃。

不得让声音、风格词或负面限制挤占镜头内容与表演要求。

## 执行流程

### 1. 解析输入

从用户和素材中确定：

- 时长、画幅与平台；
- 中心事件或几秒内的情绪变化；
- 最终画面；
- 角色采用身份优先还是情绪优先；
- 每份参考负责什么、不负责什么；
- 是否需要台词、音乐或纯环境同期声。

如果附件图像在当前界面没有显示，但用户明确说明存在及其职责，仍按用户说明处理；不要把显示缺失误判为没有使用参考图。

只询问会改变镜头数量、角色身份、核心动作或结尾的缺失信息。

### 2. 选择角色模式

- **身份优先**：固定 IP、连续系列或必须匹配脸与服装时，使用角色参考。
- **情绪优先**：几秒钟的一次性人物或微情绪变化时，可不使用角色参考；用文字定义人物，再用表演要求建立可信度。

情绪优先不等于忽略连续性。跨多个镜头时仍要保持发型、服装、面部和身体状态一致。

### 3. 根据时长决定镜头数

先确认每个候选镜头能否拥有清楚的起点、过程和结果。若时长不足，减少镜头，不压缩全部流程。

为每个镜头指定一个唯一任务。不得让后续镜头的关键动作提前串入当前镜头。

### 4. 搭建全局条件

按需填写：

- **术语解释**：定义容易被误读的人物、物体或事件性质。
- **视觉风格**：分别描述整体影像、角色呈现和环境呈现。
- **参考图说明**：为每份参考分配职责，并明确不继承的内容。

角色四视图可以只负责资产锚定；它不替代镜头内容和表演要求。背景图可以只负责场景搭建；不要从界面显示状态推断素材是否存在。

风格候选预设：

> stylized animated cinematic, semi-real stylized character, painterly realistic environment.

把它理解为整体影像／角色／环境三层风格分工，不把它当作所有任务的固定前缀。

### 5. 复制并填写镜头卡

写作前读 [references/annotated-template.md](references/annotated-template.md)，理解每个格子的职责。使用 [assets/clean-template.md](assets/clean-template.md) 作为可复制骨架。

每个镜头必须重点完成两部分：

- **镜头内容**：唯一任务、景别、水平角度、纵向角度、摄影机运动、前景／中景／后景、动作起点、动作过程、结束状态或剪辑出口。
- **表演要求**：把情绪写成眼球、眼睑、呼吸、手指、肩膀、下颌、头部、重心和节奏等可见变化。

不要只写“紧张、悲伤、坚定、虚弱”。把这些词翻译成能被看见的动作。

### 6. 补充声音

只在画面流程完成后写声音。让环境声、动作声、设备声、呼吸、台词或音乐跟随可见事件，不新增另一条抢夺注意力的叙事。

### 7. 预测崩溃并写禁止项

从本次任务推导高风险错误：身份重复、参考污染、动作串台、类型误读、表演过度、空间错误、文字／标识或平台常见伪影。只保留少量高破坏性项目。

把只影响单个镜头的风险放回该镜头，不要全部塞进全局禁止。

### 8. 交付

先输出可直接复制的完整提示词。除非用户要求解释，否则不要附带理论。若信息不足但仍可合理完成，做最小假设并保持模板简洁。

## 学习与更新本方法

当用户提供“原始提示词＋生成视频”时：

1. 先保留原始材料，不改写证据。
2. 对照提示词与成片，区分稳定复现、偶然成功、明确失败和未知来源。
3. 多个样本重复出现后，才升级为流程规则。
4. 新发现优先修改模板格子或流程顺序；只有无法被模板表达时才增加说明。

研究当前两段样本时，读 [references/sample-findings.md](references/sample-findings.md) 和 [references/original-prompt-treatment-scan.md](references/original-prompt-treatment-scan.md)，并按需检查 `assets/samples/` 中的原始视频与场景图。
