<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild static-props="component(부모)에서 child로"
    :my-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />

  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data : function () {
    return {
      dynamicProps : "It is a data"
  }},
  methods : {
    parentGetEvent(inputData){
      console.log('자이자이자식아')
      console.log(`child에서 ${inputData}를 받음`)
    },
    getDynamicData(input) {
      console.log(`child에서 입력한 ${input}을 출력 !`)
    }
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>
