<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">计量器具检定校准平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向计量标准器溯源、被检器具检定、校准证书出具、期间核查与不合格处置的一体化计量业务后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "计量标准器", path: "/stddevice" }, { label: "被检器具", path: "/instrument" }, { label: "检定规程", path: "/regulation" }, { label: "检定任务", path: "/job" }, { label: "校准证书", path: "/certificate" }, { label: "标准物质", path: "/stdmaterial" }, { label: "环境条件记录", path: "/environment" }, { label: "检定人员资质", path: "/personnel" }, { label: "期间核查", path: "/interimcheck" }, { label: "不合格处置", path: "/nonconform" }, { label: "送检委托", path: "/entrust" }, { label: "量值溯源", path: "/traceability" }, { label: "器具停用", path: "/suspension" }, { label: "复检提醒", path: "/recheck" }, { label: "检定费用", path: "/fee" }, { label: "原始记录", path: "/rawrecord" }, { label: "检定场地", path: "/site" }, { label: "抽检复核", path: "/sampling" }]
</script>
