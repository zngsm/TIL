<template>
  <div>
    <li @click="selectVideo">
      <!--video.snippet.thumbnails.medium.url 라고 쓰면 너무 길지 않나?? ==> 이걸 thumbnail.url 와 같이 별칭을 만들 수 있는 옵션 computed -->
      <img 
      :src="thumbnailUrl" 
      alt="thumbnail"
      width="320"
      height="180">
      <span>{{title }}</span>
    </li>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  props: {
    video: Object,
  },
  methods: {
    selectVideo() {
      this.$emit('select_video', this.video)
    }
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.medium.url // 반.드.시 return을 해줘야한다!!
    },
    title() {
      return _.unescape(this.video.snippet.title)
    },
  }
}
</script>

<style scoped>
  div {
    color:blue;
    background-color: black;
  }
</style>