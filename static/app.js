'use strict';

// add event listener to form, on submit
$('#new-cupcake-form').on('submit', handleFormSubmit)

// function to handle submit:
  // make axios POST request, passing form values as data
  // use response to add to page
async function handleFormSubmit(evt) {
  evt.preventDefault();

  const flavor = $('#flavor').val();
  const size = $('#size').val();
  const rating = $('#rating').val();
  const image = $('#image').val();

  const resp = await axios.post("/api/cupcakes", {flavor, size, rating, image});
  const cupcake = resp.data.cupcake;

  console.log(cupcake.image)
  $('#list-of-cupcakes').append(`<li>${cupcake.flavor}, ${cupcake.size}, ${cupcake.rating}, <img src='${cupcake.image}'></li>`)

}

// function to get all cupcakes and add to page
  // make axios GET request --> get back reponse containing all cupcakes
  //use jquery to add to html

