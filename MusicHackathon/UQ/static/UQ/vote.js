function upvote(songid){
    var url = "/upVote/"+songid
    $.get(url);
}

function downvote(songid){
    var url = "/downVote/"+songid
    $.get( url );
}
