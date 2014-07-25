



// $( "#legend" ).click(function() {
//     // $(".hide-div").slideUp();
//      $( "#test-div" ).slideToggle( "slow" );

//   });

// $( "#artifact" ).click(function() {
//     //  $(".hide-div").slideUp();
//     $( "#test-div-2" ).slideToggle( "slow" );
//   });

// function showMessage(msg) {
//   alert(msg);
// };

$('.types-button').click(function(e){
    var store_data = $(this).attr('data');
    if(store_data == 'enchant'){
        // alert('enchant');
        showContent(store_data);
    }else if(store_data == 'legend'){
        alert("legend");
        showContent(store_data);
    }else if(store_data == 'artifact'){
        alert("artifact");
        showContent(store_data);
    }

});


function showContent(div){
    $("#types-div").slideUp();
    $("#types-div").slideDown();
    $("#types-div.div.jumbotron").append("dafsd  jjj  afasdfsajjjj");
    // $(".jumbotron").append("dafsdafasdfsa sadf sadf sadf ");
}