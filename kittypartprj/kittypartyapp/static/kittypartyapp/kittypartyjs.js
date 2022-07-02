jQuery(document).ready(function () {
    var btncheck=document.getElementById('btncheck')
    var divcheck=document.getElementById('divcheck')
    var txtcheck=document.getElementById('txtcheck')
    var hdcheck=document.getElementById('hdcheck')
function clickonchk(event){
    
    hdcheck.value=hdcheck.value + " " +event.target.value
    console.log(hdcheck.value)
}
function createcheckbox(){
    var myDiv = document.getElementById("divcheck");
             
            // creating checkbox element
            var checkbox = document.createElement('input');
             
            // Assigning the attributes
            // to created checkbox
            for (let i = 0; i < 5; i++) {                
            checkbox = document.createElement('input');
            checkbox.type = "checkbox";
            checkbox.name = "name";
            checkbox.value = i.toString();
            checkbox.id = "id" +toString();
            checkbox.addEventListener('click',clickonchk)
            myDiv.appendChild(checkbox);
        }
}
btncheck.addEventListener('click',createcheckbox)
    $("#containergame").children().prop('disabled', true);
    $('#containergame *').prop('disabled', true);
    $('.datepicker').datepicker({ 'dateFormat': 'yy-mm-dd' });
jQuery('#id_gameid').select2()
$("select[id$='-course']").select2({
    'placeholder':"Select Course",
    'width':'150px'
})

    var gameid = 'gameid'
    var course='course'
    
    jQuery('#btnSaveParty').click(function () {
        jQuery('#idgame').toggle()
    })

    jQuery('#btnShowInvitee').click(function () {
        jQuery('#dividinvitee').toggle()
    })
    $(document).on('change', 'select', function (e) {
        e.preventDefault();
        
        var mygame = $(this).find('option:selected').text();
        var myid = $(this)[0].id
        var gameset = jQuery('select[name$="' + gameid + '"]')
        gameset.each(function (index, item) {
            var $option = $(this).find('option:selected')
            console.log(mygame)
            console.log($option.text())
            if ($(this)[0].id != myid) {
                if (mygame == $option.text()) {
                    jQuery("#" + myid).prop('selectedIndex', 0);

                }
            }
        })
        return false;
    });
    $('#add_more').click(function () {
        var form_idx = $('#id_gamepartybridge_set-TOTAL_FORMS').val();
        $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
        $('#id_gamepartybridge_set-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });
    function destroySelect2(){
        var hi= jQuery('select[name$="' + course + '"]')
        
        hi.select2('destroy')
        $('.datepicker').datepicker('destroy');
    
    }
    function initailizeSelect2(){
        var hi= jQuery('select[name$="' + course + '"]')
        $(".datepicker").datepicker({dateFormat: 'yy-mm-dd'});
        hi.select2({
            dropdownAutoWidth : true,
            width:100,
            theme: "classic"
        })
    }
    jQuery('#btnAddMoreCourse').click(function(event){
        let container = document.querySelector(".course_container")
        let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
        event.preventDefault()
        let gameForm = document.querySelectorAll(".course_container li")
        let gameFormUI=document.querySelector(".course_container")
        totalforms=document.querySelector("#id_form-TOTAL_FORMS")
        let formNum=gameForm.length-1
        formNum++
        destroySelect2()
        let newliNode=gameForm[0].cloneNode(true)
        let formRegex = RegExp(`form-(\\d){1}-`,'g')
        newliNode.innerHTML=newliNode.innerHTML.replace(formRegex,`form-${formNum}-`)
      
       
      
        // myselect.selectedIndex=0
        gameFormUI.appendChild(newliNode)
       
        totalforms.setAttribute('value', `${formNum+1}`)
        initailizeSelect2()
        
    //     let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
    //     trtobeadded=document.querySelector(".emptytr")
    //     var trhtml='<tr>'+trtobeadded.innerHTML+'</tr>'
    //     let trcount=jQuery('#tblcoursetbody tr').length
    //     trcount=trcount-2
    //     let formRegex = RegExp(`form_set-(\\d){1}-`,'g')
        
    //     trhtml=trhtml.replace(/__prefix__/g,`${trcount}`)
        
        
    //    console.log( jQuery('#id_form-'+trcount+'-course').html)
        
    //     jQuery('#coursetbody').append(trhtml)
        
    //     jQuery('#id_form-'+trcount+'-startdate').addClass('startdate')        
    //     jQuery('#id_form-'+trcount+'-startdate').removeClass('datepicker')
    //     jQuery('#id_form-'+trcount+'-startdate').removeClass('hasDatepicker')
    //     jQuery('.startdate').datepicker({})
    //     jQuery('#id_form-'+trcount+'-course').removeClass('select2')
    //     jQuery('#id_form-'+trcount+'-course').removeClass('django-select2')
    //     jQuery('#id_form-'+trcount+'-course').select2('destroy')
    //     jQuery('#id_form-'+trcount+'-course').removeClass('select2-hidden-accessible')
    //     jQuery('#id_form-'+trcount+'-course').select2()
    //     var n=trtobeadded.children

       
        
        
    //     jQuery('#id_form-'+trcount+'-course').select2()
    })
  
  jQuery('#btngetconcatevalue').click(function(event){
     jQuery.ajax({
         type:'GET',
         url:'/chikku',
         success:function(data){
             console.log(data)
             console.log(data[0].partyname)
         }
     })
  })
  jQuery('#backindemand').click(function(){
    //   history.back()
    //   alert(history)
    //   alert(jQuery('#txtjobcard').val())
  })
  jQuery('#id_form-0-jobcard').change(function(event){
      alert('am changing')
      jobcard=jQuery(this).val()
    jQuery('#hdjobcarddemand').val(jobcard)
    jQuery('#hdjobcardparts').val(jobcard)
  })
    jQuery('#AddMoreGames').click(function(event){
        let container = document.querySelector("#form-container")
        let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
        event.preventDefault()
        let gameForm = document.querySelectorAll(".game_container li")
        let gameFormUI=document.querySelector(".game_container")
        totalforms=document.querySelector("#id_gamepartybridge_set-TOTAL_FORMS")
        let formNum=gameForm.length-1
        formNum++
        let newliNode=gameForm[0].cloneNode(true)
        let formRegex = RegExp(`gamepartybridge_set-(\\d){1}-`,'g')
        newliNode.innerHTML=newliNode.innerHTML.replace(formRegex,`gamepartybridge_set-${formNum}-`)
        myselect=newliNode.querySelector('select')
        myselect.selectedIndex=0
        gameFormUI.appendChild(newliNode)
        totalforms.setAttribute('value', `${formNum+1}`)
        
        
    })
    jQuery('select[name$="' + gameid + '"]').change(function () {

        var mygame = $(this).find('option:selected').text();
        var myid = $(this)[0].id
        var gameset = jQuery('select[name$="' + gameid + '"]')
        gameset.each(function (index, item) {
            var $option = $(this).find('option:selected')
            console.log(mygame)
            console.log($option.text())
            if ($(this)[0].id != myid) {
                if (mygame == $option.text()) {
                    jQuery("#" + myid).prop('selectedIndex', 0);

                }
            }
        })

        // jQuery("#" + myid).prop('selectedIndex', 0);

    })

})