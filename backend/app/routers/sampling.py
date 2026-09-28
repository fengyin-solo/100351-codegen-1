"""抽检复核接口：维护抽检复核单，覆盖发起抽检、提交结论、判定不合格等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.sampling import SamplingService

router = APIRouter(prefix="/api/sampling", tags=["抽检复核"])

service = SamplingService()

LIST_FIELDS = ["抽检编号", "抽检批次", "抽检数量", "抽检依据", "抽检结论", "抽检人", "抽检日期", "抽检状态"]
STATUSES = ["待抽检", "抽检中", "抽检合格", "抽检不合格"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按抽检编号检索"),
    status: str | None = Query(default=None, description="待抽检、抽检中、抽检合格、抽检不合格"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按抽检编号与状态过滤抽检复核列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条抽检复核单明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"抽检复核单 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条抽检复核单，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="抽检复核单已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条抽检复核单执行发起抽检、提交结论、判定不合格；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出抽检复核清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "sampling", "total": total, "items": items}
