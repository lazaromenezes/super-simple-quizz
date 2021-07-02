function vote(city){
  let payload = `{ "city": "${city}" }`
  $.post("/api/SaveVote", payload, afterPost)
}

function afterPost(data){
  $.get("/api/ShowResults", showResults)
}

function showResults(results){
  let total = results.total

  let resultsContainer = $("#results")
  resultsContainer.html("")

  addResult(results.amsterdam, 'Amsterdã', total, resultsContainer)
  addResult(results.munique, 'Munique', total, resultsContainer)
  addResult(results.paris, 'Paris', total, resultsContainer)
  addResult(results.veneza, 'Veneza', total, resultsContainer)
}

function addResult(votes, label, total, container){
  let percent = (votes || 0) / total * 100.00
  percent = percent.toFixed(2)

  let labelElement = $("<div>")
  labelElement.text(label)

  let result = $("<div>")
  result.addClass('resultItem z-depth-3 red accent-1 valign-wrapper')
  result.html(`${percent} %`)

  labelElement.appendTo(container)
  result.appendTo(container)

  result.animate({width: `${percent}%`}, 500)
}
