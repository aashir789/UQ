function upvote(songid){
    $.get( "/upVote", { id: "songid" } );
}

function downvote(songid){
    $.get( "/upVote", { id: "songid" } );
}
