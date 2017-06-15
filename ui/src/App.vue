<template>
  <div id="app">
    <ais-index
      appId="WTS23NLS2K"
      apiKey="a49fed1a512e605d8356722bfbb84ebe"
      indexName="ICD10Code"
    >
      <ais-search-box />
      <ais-results>
        <template scope="{ result }">
          <h2>
            <ais-highlight :result="result" attributeName="code" >
            </ais-highlight>:
            <ais-highlight :result="result" attributeName="path" >
            </ais-highlight>
          </h2>
        </template>
      </ais-results>
    </ais-index>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
