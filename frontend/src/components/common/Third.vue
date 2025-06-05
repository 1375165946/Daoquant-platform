<template>
  <section class="strategy-selection">
    <h2 class="section-title">策略精选</h2>
    <div class="card-container">
      <div v-for="(item, index) in strategies" :key="index" class="strategy-card">
        <router-link :to="`/strategy/${item.id}`">
          <img :src="item.image" class="strategy-chart" />
        </router-link>
        <h3 class="strategy-title">{{ item.title }}</h3>
        <div class="strategy-info">
          <div class="info-row">
            <span>年化收益</span>
            <span class="highlight">{{ item.annualReturn }}</span>
            <span>最大回撤</span>
            <span>{{ item.maxDrawdown }}</span>
            <span>初始资金</span>
            <span>{{ item.capital }}</span>
          </div>
        </div>
        <div class="strategy-footer">
          <span>{{ item.userCount }}人已获取源码</span>
          <router-link :to="`/strategy/${item.id}/source`">
            <button class="get-btn">获取源码</button>
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const strategies = [
  {
    id: 1,
    title: '价值选股与RSRS择时',
    image: '/images/common/lbt1.jpg',
    annualReturn: '21.9%',
    maxDrawdown: '11.9%',
    capital: '500000',
    userCount: '8046',
  },
  {
    id: 2,
    title: '【量化课堂】机器学习多因子策略',
    image: '/images/common/lbt2.jpg',
    annualReturn: '34.2%',
    maxDrawdown: '25.4%',
    capital: '10000000',
    userCount: '7490',
  },
  {
    id: 3,
    title: '股指期货跨期套利策略',
    image: '/images/common/lbt3.jpg',
    annualReturn: '56.1%',
    maxDrawdown: '17.1%',
    capital: '1000000',
    userCount: '14626',
  },
]
</script>

<style  scoped>
  @import '@/assets/css/common/Third.css';
</style>
