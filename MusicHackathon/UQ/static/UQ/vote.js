function upvote(songid){
    var url = "/upVote/"+songid
    $.get(url, function(data){
	ele = document.getElementById('song'+songid);
	eleVal = parseInt(ele.innerHTML)+1;
	
	ele.innerHTML= eleVal; 
    });
}

function downvote(songid){
    var url = "/downVote/"+songid
    $.get(url, function(data){
	ele = document.getElementById('song'+songid);
	eleVal = parseInt(ele.innerHTML)-1;
	
	ele.innerHTML= eleVal; 
    });
}
