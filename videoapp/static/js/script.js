$(document).ready(function(){
    $(".segmented label input[type=radio]").each(function(){
        $(this).on("change", function(){
            if($(this).is(":checked")){
                
               $(this).parent().siblings().each(function(){
                    $(this).removeClass("checked");
                });
                $(this).parent().addClass("checked");

                //sort post items
                var sortparam = this.nextSibling.nodeValue;
                var $postlist = $('#post-list-id'),
                $postlistchildren = $postlist.children('div');
                
                $postlistchildren.sort(function(a,b){
                var an = a.getAttribute('data-' + sortparam),
                    bn = b.getAttribute('data-' + sortparam);  
            
                if(an > bn) {
                    return -1;
                }
                if(an < bn) {
                    return 1;
                }
                return 0;
                });
                
                $postlistchildren.detach().appendTo($postlist);

            }
        });
    });

    $(".theater-video").each(function(){
        $(this).on('play', function(){
            //update view count
            var postuuid = $(this).attr('data-uuid');
            
            $.ajax({
                url : /view/ + postuuid,
                type: "GET",
                data : {csrfmiddlewaretoken: CSRF_TOKEN},
                dataType : "json",
                success: function( data ){
                    // do something
                    alert("view updated");
                }
            });

        })
    })
});