"""复检提醒接口：维护复检提醒单，覆盖发出提醒、确认复检、忽略提醒等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.recheck import RecheckService

router = APIRouter(prefix="/api/recheck", tags=["复检提醒"])

service = RecheckService()

LIST_FIELDS = ["提醒编号", "关联器具", "上次检定日", "下次检定日", "剩余天数", "提醒方式", "提醒人", "提醒状态"]
STATUSES = ["待提醒", "已提醒", "已复检", "已忽略"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按提醒编号检索"),
    status: str | None = Query(default=None, description="待提醒、已提醒、已复检、已忽略"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按提醒编号与状态过滤复检提醒列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条复检提醒单明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"复检提醒单 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条复检提醒单，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="复检提醒单已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条复检提醒单执行发出提醒、确认复检、忽略提醒；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出复检提醒清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "recheck", "total": total, "items": items}
