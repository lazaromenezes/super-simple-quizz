function vote(city){
  payload = { city: city }
  $.post("/api/SaveVote", payload, (data) => {
    alert('Vote saved!')
  })
}
