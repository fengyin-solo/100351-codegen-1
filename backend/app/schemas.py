"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class StddeviceEntry(BaseModel):
    """计量标准器明细结构。"""

    field_0: str | None = None  # 标准器编号
    field_1: str | None = None  # 标准器名称
    field_2: str | None = None  # 准确度等级
    field_3: str | None = None  # 测量范围
    field_4: str | None = None  # 溯源机构
    field_5: str | None = None  # 证书编号
    field_6: str | None = None  # 有效截止日
    field_7: str | None = None  # 标准器状态

class InstrumentEntry(BaseModel):
    """被检器具明细结构。"""

    field_0: str | None = None  # 器具编号
    field_1: str | None = None  # 器具名称
    field_2: str | None = None  # 规格型号
    field_3: str | None = None  # 测量范围
    field_4: str | None = None  # 使用部门
    field_5: str | None = None  # 存放位置
    field_6: str | None = None  # 上次检定日
    field_7: str | None = None  # 器具状态

class RegulationEntry(BaseModel):
    """检定规程明细结构。"""

    field_0: str | None = None  # 规程编号
    field_1: str | None = None  # 规程名称
    field_2: str | None = None  # 适用器具
    field_3: str | None = None  # 检定周期
    field_4: str | None = None  # 主要检定项目
    field_5: str | None = None  # 环境要求
    field_6: str | None = None  # 版本号
    field_7: str | None = None  # 规程状态

class JobEntry(BaseModel):
    """检定任务单明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 关联规程
    field_2: str | None = None  # 受检器具数
    field_3: str | None = None  # 计划开始日
    field_4: str | None = None  # 计划完成日
    field_5: str | None = None  # 检定班组
    field_6: str | None = None  # 检定员
    field_7: str | None = None  # 任务状态

class CertificateEntry(BaseModel):
    """校准证书明细结构。"""

    field_0: str | None = None  # 证书编号
    field_1: str | None = None  # 受检器具
    field_2: str | None = None  # 检定结论
    field_3: str | None = None  # 检定日期
    field_4: str | None = None  # 检定员
    field_5: str | None = None  # 复核员
    field_6: str | None = None  # 出具日期
    field_7: str | None = None  # 证书状态

class StdmaterialEntry(BaseModel):
    """标准物质明细结构。"""

    field_0: str | None = None  # 物质编号
    field_1: str | None = None  # 物质名称
    field_2: str | None = None  # 浓度标称值
    field_3: str | None = None  # 扩展不确定度
    field_4: str | None = None  # 批号
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 存储条件
    field_7: str | None = None  # 物质状态

class EnvironmentEntry(BaseModel):
    """环境条件记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所在实验室
    field_2: str | None = None  # 温度示值
    field_3: str | None = None  # 相对湿度
    field_4: str | None = None  # 大气压力
    field_5: str | None = None  # 记录日期
    field_6: str | None = None  # 记录人
    field_7: str | None = None  # 环境状态

class PersonnelEntry(BaseModel):
    """检定人员明细结构。"""

    field_0: str | None = None  # 人员编号
    field_1: str | None = None  # 人员姓名
    field_2: str | None = None  # 持证项目
    field_3: str | None = None  # 证书等级
    field_4: str | None = None  # 发证机构
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 所在班组
    field_7: str | None = None  # 资质状态

class InterimcheckEntry(BaseModel):
    """期间核查记录明细结构。"""

    field_0: str | None = None  # 核查编号
    field_1: str | None = None  # 核查对象
    field_2: str | None = None  # 核查方式
    field_3: str | None = None  # 核查日期
    field_4: str | None = None  # 核查结论
    field_5: str | None = None  # 偏差值
    field_6: str | None = None  # 核查人
    field_7: str | None = None  # 核查状态

class NonconformEntry(BaseModel):
    """不合格处置单明细结构。"""

    field_0: str | None = None  # 处置编号
    field_1: str | None = None  # 关联器具
    field_2: str | None = None  # 不合格项
    field_3: str | None = None  # 不合格描述
    field_4: str | None = None  # 处置方式
    field_5: str | None = None  # 责任班组
    field_6: str | None = None  # 处置期限
    field_7: str | None = None  # 处置状态

class EntrustEntry(BaseModel):
    """送检委托单明细结构。"""

    field_0: str | None = None  # 委托单号
    field_1: str | None = None  # 委托单位
    field_2: str | None = None  # 送检器具数
    field_3: str | None = None  # 期望完成日
    field_4: str | None = None  # 联系人
    field_5: str | None = None  # 联系电话
    field_6: str | None = None  # 取件方式
    field_7: str | None = None  # 委托状态

class TraceabilityEntry(BaseModel):
    """量值溯源记录明细结构。"""

    field_0: str | None = None  # 溯源编号
    field_1: str | None = None  # 溯源项目
    field_2: str | None = None  # 上级机构
    field_3: str | None = None  # 溯源方式
    field_4: str | None = None  # 溯源日期
    field_5: str | None = None  # 溯源结果
    field_6: str | None = None  # 溯源人员
    field_7: str | None = None  # 溯源状态

class SuspensionEntry(BaseModel):
    """器具停用单明细结构。"""

    field_0: str | None = None  # 停用单号
    field_1: str | None = None  # 停用器具
    field_2: str | None = None  # 停用原因
    field_3: str | None = None  # 停用日期
    field_4: str | None = None  # 影响岗位
    field_5: str | None = None  # 审批人
    field_6: str | None = None  # 预计恢复日
    field_7: str | None = None  # 停用状态

class RecheckEntry(BaseModel):
    """复检提醒单明细结构。"""

    field_0: str | None = None  # 提醒编号
    field_1: str | None = None  # 关联器具
    field_2: str | None = None  # 上次检定日
    field_3: str | None = None  # 下次检定日
    field_4: str | None = None  # 剩余天数
    field_5: str | None = None  # 提醒方式
    field_6: str | None = None  # 提醒人
    field_7: str | None = None  # 提醒状态

class FeeEntry(BaseModel):
    """检定费用单明细结构。"""

    field_0: str | None = None  # 费用单号
    field_1: str | None = None  # 委托单位
    field_2: str | None = None  # 器具数量
    field_3: str | None = None  # 计费单价
    field_4: str | None = None  # 应收金额
    field_5: str | None = None  # 减免金额
    field_6: str | None = None  # 收费日期
    field_7: str | None = None  # 费用状态

class RawrecordEntry(BaseModel):
    """原始记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 检定项目
    field_3: str | None = None  # 实测值
    field_4: str | None = None  # 允许误差
    field_5: str | None = None  # 判定结果
    field_6: str | None = None  # 记录员
    field_7: str | None = None  # 记录状态

class SiteEntry(BaseModel):
    """检定场地明细结构。"""

    field_0: str | None = None  # 场地编号
    field_1: str | None = None  # 场地名称
    field_2: str | None = None  # 使用面积
    field_3: str | None = None  # 恒温能力
    field_4: str | None = None  # 振动等级
    field_5: str | None = None  # 电磁屏蔽等级
    field_6: str | None = None  # 使用班组
    field_7: str | None = None  # 场地状态

class SamplingEntry(BaseModel):
    """抽检复核单明细结构。"""

    field_0: str | None = None  # 抽检编号
    field_1: str | None = None  # 抽检批次
    field_2: str | None = None  # 抽检数量
    field_3: str | None = None  # 抽检依据
    field_4: str | None = None  # 抽检结论
    field_5: str | None = None  # 抽检人
    field_6: str | None = None  # 抽检日期
    field_7: str | None = None  # 抽检状态
