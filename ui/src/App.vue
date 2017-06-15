<template>
  <div id="app">
    <ais-index
      appId="WTS23NLS2K"
      apiKey="a49fed1a512e605d8356722bfbb84ebe"
      indexName="ICD10Code"
    >
      <center>
        <ais-search-box />
        <ais-stats />
        <ais-pagination></ais-pagination>
      </center>
      <hr/>
      <ais-results>
        <template scope="{ result }">
          <div class='search-result'>
            <a @click.stop='codeSelected(result.code)' href='#' >
            <ais-highlight
              :result="result" attributeName="code" >
            </ais-highlight>
            </a>
            <ais-highlight :result="result" attributeName="path" >
            </ais-highlight>
            </a>
          </div>
        </template>
      </ais-results>
    </ais-index>
    <hr/>
    <center><ais-powered-by></ais-powered-by></center>
  </div>
</template>

<script>
export default {
  name: 'app',
  methods: {
    codeSelected (code) {
      console.log(code)
    }
  }
}
</script>

<style>
ul.ais-pagination{
  list-style-type: none;
  text-align: center;
}
ul.ais-pagination li {
  display: inline;
  margin:10px;
}
.search-result{
  padding:10px;
  border: solid 1px #f1f1f1;
}
</style>
