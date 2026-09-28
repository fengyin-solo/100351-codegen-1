import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Stddevice = () => import('@/views/stddevice/index.vue')
const Instrument = () => import('@/views/instrument/index.vue')
const Regulation = () => import('@/views/regulation/index.vue')
const Job = () => import('@/views/job/index.vue')
const Certificate = () => import('@/views/certificate/index.vue')
const Stdmaterial = () => import('@/views/stdmaterial/index.vue')
const Environment = () => import('@/views/environment/index.vue')
const Personnel = () => import('@/views/personnel/index.vue')
const Interimcheck = () => import('@/views/interimcheck/index.vue')
const Nonconform = () => import('@/views/nonconform/index.vue')
const Entrust = () => import('@/views/entrust/index.vue')
const Traceability = () => import('@/views/traceability/index.vue')
const Suspension = () => import('@/views/suspension/index.vue')
const Recheck = () => import('@/views/recheck/index.vue')
const Fee = () => import('@/views/fee/index.vue')
const Rawrecord = () => import('@/views/rawrecord/index.vue')
const Site = () => import('@/views/site/index.vue')
const Sampling = () => import('@/views/sampling/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/stddevice', name: 'stddevice', component: Stddevice },
    { path: '/instrument', name: 'instrument', component: Instrument },
    { path: '/regulation', name: 'regulation', component: Regulation },
    { path: '/job', name: 'job', component: Job },
    { path: '/certificate', name: 'certificate', component: Certificate },
    { path: '/stdmaterial', name: 'stdmaterial', component: Stdmaterial },
    { path: '/environment', name: 'environment', component: Environment },
    { path: '/personnel', name: 'personnel', component: Personnel },
    { path: '/interimcheck', name: 'interimcheck', component: Interimcheck },
    { path: '/nonconform', name: 'nonconform', component: Nonconform },
    { path: '/entrust', name: 'entrust', component: Entrust },
    { path: '/traceability', name: 'traceability', component: Traceability },
    { path: '/suspension', name: 'suspension', component: Suspension },
    { path: '/recheck', name: 'recheck', component: Recheck },
    { path: '/fee', name: 'fee', component: Fee },
    { path: '/rawrecord', name: 'rawrecord', component: Rawrecord },
    { path: '/site', name: 'site', component: Site },
    { path: '/sampling', name: 'sampling', component: Sampling },
  ],
})

export default router
