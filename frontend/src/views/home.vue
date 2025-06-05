<template>
  <div class="home-container">
    <!-- 固定顶部导航栏 -->
    <FixedNavbar />

    <!-- 可滚动内容区域 -->
    <div>
      <Second />
      <Third />
      <Four/>
      <Six/>
      <Five/>
      <Lastone/>
    </div>
  </div>
</template>

<script setup>
import FixedNavbar from '@/components/common/FixedNavbar.vue'
import Second from '@/components/common/Second.vue'
import Third from '@/components/common/Third.vue';
import Four from '@/components/common/Four.vue';
import Five from '@/components/common/Five.vue';
import Six from '@/components/common/Six.vue';
import Lastone from '@/components/common/Lastone.vue';

</script>