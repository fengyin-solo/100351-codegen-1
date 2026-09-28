"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import stddevice as router_stddevice
from app.routers import instrument as router_instrument
from app.routers import regulation as router_regulation
from app.routers import job as router_job
from app.routers import certificate as router_certificate
from app.routers import stdmaterial as router_stdmaterial
from app.routers import environment as router_environment
from app.routers import personnel as router_personnel
from app.routers import interimcheck as router_interimcheck
from app.routers import nonconform as router_nonconform
from app.routers import entrust as router_entrust
from app.routers import traceability as router_traceability
from app.routers import suspension as router_suspension
from app.routers import recheck as router_recheck
from app.routers import fee as router_fee
from app.routers import rawrecord as router_rawrecord
from app.routers import site as router_site
from app.routers import sampling as router_sampling

ROUTERS = [router_stddevice, router_instrument, router_regulation, router_job, router_certificate, router_stdmaterial, router_environment, router_personnel, router_interimcheck, router_nonconform, router_entrust, router_traceability, router_suspension, router_recheck, router_fee, router_rawrecord, router_site, router_sampling]
