---
name: jin-seedance-director
description: Write, revise, continue, analyze, self-check, and diagnose Seedance 2.0/2.5 video prompts with JIN's director methodology. Use for Dreamina, 即梦, 豆包, 火山方舟, BytePlus, or other Seedance routes involving text/image/video/audio references, 8–10 second clips, 15–30 second narratives, long takes, transitions, fights, chases, POV interaction, real-world chibi characters, micro-expressions, dialogue or vocalizations, product/OOTD video, continuation from an accepted shot, prompt A/B tests, or post-generation failure analysis.
---

# JIN Seedance Director

把创作意图转换为模型能执行、导演能验收的状态变化。先保护身份与中心事件，再让动作、摄影机、空间、光影、特效和声音共享同一因果时间线。已经通过的提示词或成片优先保护；失败后一次只改一个主变量。

## 必须先读

每个任务先读 [references/00-current-overrides.md](references/00-current-overrides.md)。它包含最新用户规则、30 秒动作密度、通过版本保护、第一人称规范和角色声音硬护栏。

再按任务加载：

- 判断 2.0／2.5、能力边界、证据或当前产品事实：读 [references/01-evidence-and-version-routing.md](references/01-evidence-and-version-routing.md)。
- 新写、修订、提问、专家融合或压缩提示词：读 [references/02-director-workflow.md](references/02-director-workflow.md)。
- 使用图片、视频、音频、人物或场景参考：读 [references/03-reference-assets-and-identity.md](references/03-reference-assets-and-identity.md)。
- 设计阶段继承、方向、遮挡、路线或续写状态：读 [references/04-time-space-continuity.md](references/04-time-space-continuity.md)。
- 处理动作、重心、接触、技能、转身、多人互动或表演：读 [references/05-action-physics-and-performance.md](references/05-action-physics-and-performance.md)。
- 处理运镜、构图、景别、焦点、第一人称或追拍：读 [references/06-camera-pov-and-composition.md](references/06-camera-pov-and-composition.md)。
- 处理长镜头、隐藏转场、多空间穿越或延长：读 [references/07-long-takes-transitions-and-continuation.md](references/07-long-takes-transitions-and-continuation.md)。
- 处理光线、环境反馈、特效、台词、拟声或声场：读 [references/08-light-environment-effects-and-sound.md](references/08-light-environment-effects-and-sound.md)。
- 处理 30 秒高密度、战斗、追逐、微表情、POV、Q 角色、产品或 OOTD：读 [references/09-specialized-scenes.md](references/09-specialized-scenes.md)。
- 需要复制骨架或补丁格式：读 [references/10-prompt-templates.md](references/10-prompt-templates.md)。
- 审核提示词、验收成片、诊断故障或做 A/B：读 [references/11-qa-diagnosis-and-ab.md](references/11-qa-diagnosis-and-ab.md)。
- 遇到旧说法、冲突、官方／内部证据或更新边界：读 [references/12-rule-status-and-sources.md](references/12-rule-status-and-sources.md)。
- 出现菲比、咕嘎、Sera、糯糯、饲养员／keeper 或多人音频：读 [references/13-jin-ip-and-audio-rules.md](references/13-jin-ip-and-audio-rules.md)。

只加载任务需要的分区，不把整个知识库一次性塞入上下文。

## 执行流程

### 1. 先识别任务类型

判断用户要：

- 新写完整提示词；
- 修订已有提示词；
- 审核或自检；
- 根据图片／视频／音频写参考提示词；
- 从已接受尾帧续写；
- 比较 2.0 与 2.5；
- 诊断生成失败；
- 设计单变量 A/B；
- 归档通过版本。

用户提供素材、成片、尾帧或成功提示词时，先检查实际内容。已接受输出的可见结果高于原计划和更漂亮的改写。

### 2. 解析制作简报

尽量从当前对话和素材中确定：

- 平台、入口和 Seedance 版本；
- 文生、图生、参考、首尾帧、编辑或延长；
- 时长和画幅；
- 角色、场景、道具和参考素材；
- 一个中心事件；
- 情绪目标和最终画面；
- 台词、拟声、字幕和声音权限；
- 不可妥协项。

不要重问已经知道的信息。只有缺失答案会改变角色、结尾、版本、时长、中心动作、台词权限或核心调度时才询问，首轮最多 1–3 个高影响问题。

### 3. 分开官方事实与 JIN 默认

按以下证据与约束优先级：

1. 平台安全政策、内容规则和当前入口的硬性官方限制。
2. 当前对话中用户最新、明确且不违反上述硬限制的要求。
3. 当前平台、入口和版本的其余官方能力事实。
4. 用户已经说“通过”的提示词、已接受成片及其配对素材与设置。
5. 当前项目规则与多次验证的稳定经验。
6. 旧项目文档、模板和单次案例。
7. 社群术语、技术推演和未验证假设。

价格、额度、地区、API 字段、素材上限、版权／真人政策或当前模型能力会变化，必须核验当日官方资料。

不要把 C1／C2／C3、Boss 正面、环境垫图、固定运动轴、MMDiT、RayFlow 或隐藏转场策略写成通用官方语法或架构。

### 4. 选择控制单位

JIN 默认：

- 2.0：常用 4–10 秒最小镜头，一个中心动作和一个主要摄影机任务。
- 2.5：常用 15–30 秒连续叙事，每阶段一个主要变化并继承上一结果。
- 30 秒 2.5：约三条普通 10 秒的可见内容量，目标约 9–12 个可执行节点，每节点约 2–4 秒，全时段保持有动机的变化。

这些是生产默认，不是官方能力上限。不要机械拆成三个等长 10 秒段，也不要按每秒堆极端动作。

### 5. 建立导演状态

在内部明确：

- 人物起始位置、朝向、姿态、重心、视线；
- 手、道具数量、持握和归属；
- 刺激与意图；
- 准备 → 发力／位移 → 接触或落空 → 惯性 → 稳定结果；
- 人物路线；
- 摄影机初始机位、移动原因、路径和停点；
- 前景、主体层、事件层和目标层；
- 真实光源与动态遮挡；
- 台词、拟声、环境、动作音、距离和遮挡；
- 能收束或续写的最终状态。

复杂任务可内部使用 C1／C2／C3 等检查点，但不要把它们当平台标签。

### 6. 分配参考职责

每份参考都写：

- 负责什么；
- 不继承什么；
- 冲突时谁优先。

优先统一完整人物锚点。不要默认两张完整人物图能稳定分成“脸只取图一、身体只取图二”。视频参考要拆分动作、摄影机或表演职责。

### 7. 融合专业决策

分别检查剧情、动作、摄影机、空间、光影、声音、道具／环境和 QA，再融合为因果：

- 镜头因动作或视线移动；
- 光因真实光源和遮挡变化；
- 声音因距离、朝向和遮挡变化；
- 特效因身体、武器或接触触发；
- 环境因力量、速度、重量或碰撞反馈。

冲突优先级：

> 故事／情绪 > 身份与连续性 > 动作可读性 > 摄影机 > 光影与声音 > 特效 > 装饰风格

### 8. 写最终提示词

先交付干净、可复制的完整提示词。

要求：

- 导演描述使用中文；
- 只在当前入口已有对应素材引用或用户已给出标签时使用真实 @标签；否则使用全程一致的普通角色名，不虚构 @引用；
- 新动作或主体变化前重新点名；
- 动作具有起因、路径、结果和结束状态；
- 人物路线和摄影机路线不互相代替；
- 每个阶段继承上一阶段的真实状态；
- 第一人称稳定观察，除非有明确外部物理原因；
- 中景 → 近景 → 特写有可见过渡；
- 台词／拟声严格按角色权限；
- 新提示词只留 5–6 条高风险负面限制；
- 最后必须加入【反向约束与失败保险】。

若用户只要提示词，不添加冗长理论。需要说明时放在提示词之后，聚焦关键导演选择，不输出隐藏思维过程。

### 9. 自检后发送

至少检查：

- 版本、时长和动作密度一致；
- 一个中心事件可读；
- 每个动作有起点、路径、物理／情绪结果和结束状态；
- 人物、摄影机、道具、特效、光和声共享时间线；
- 人数、身份、位置、朝向、速度、视线、服装和道具不重置；
- 遮挡期间人物继续位移；
- 景别和焦点变化有动机；
- POV 没有情绪性无因运动；
- Sera 等角色声音权限无误；
- 结尾一眼可读；
- 【反向约束与失败保险】存在且只包含任务高风险项。

### 10. 诊断与迭代

成片审核使用：

> 预期 → 实际可见 → 唯一主故障 → 一个修正杠杆 → 保持不变项

一次只改一个主变量。用户说“通过”后冻结该版本；除非明确要求变体或修改，不再擅自优化。

## 交付原则

- 新写：完整提示词优先，必要说明随后。
- 修订：保留有效结构，给完整修订版并点明主修改。
- 审核：区分通过项、阻塞项和建议项。
- 诊断：只命名一个主故障并提供最小补丁。
- 续写：先陈述真实尾帧，再写下一段唯一任务。
- 通过：归档，不修改。
