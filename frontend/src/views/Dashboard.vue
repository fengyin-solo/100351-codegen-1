<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "计量标准器", "created": 0, "pending": 0, "abnormal": 0}, {"name": "被检器具", "created": 0, "pending": 0, "abnormal": 0}, {"name": "检定规程", "created": 0, "pending": 0, "abnormal": 0}, {"name": "检定任务", "created": 0, "pending": 0, "abnormal": 0}, {"name": "校准证书", "created": 0, "pending": 0, "abnormal": 0}, {"name": "标准物质", "created": 0, "pending": 0, "abnormal": 0}, {"name": "环境条件记录", "created": 0, "pending": 0, "abnormal": 0}, {"name": "检定人员资质", "created": 0, "pending": 0, "abnormal": 0}, {"name": "期间核查", "created": 0, "pending": 0, "abnormal": 0}, {"name": "不合格处置", "created": 0, "pending": 0, "abnormal": 0}, {"name": "送检委托", "created": 0, "pending": 0, "abnormal": 0}, {"name": "量值溯源", "created": 0, "pending": 0, "abnormal": 0}, {"name": "器具停用", "created": 0, "pending": 0, "abnormal": 0}, {"name": "复检提醒", "created": 0, "pending": 0, "abnormal": 0}, {"name": "检定费用", "created": 0, "pending": 0, "abnormal": 0}, {"name": "原始记录", "created": 0, "pending": 0, "abnormal": 0}, {"name": "检定场地", "created": 0, "pending": 0, "abnormal": 0}, {"name": "抽检复核", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
