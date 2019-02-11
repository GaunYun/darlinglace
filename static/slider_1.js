var slider1ratio;
var slider1tobeadded;
var zahl;
var table_loaded;

var slider = new Slider(document.getElementById('slider'),64, 111);
slider.onChange = function(value) {

    //document.getElementById('value').textContent = Math.round(value);
};


function Slider(container, minValue, maxValue) {
    var slider = this;
    		slider1ratio=0.47;
    		slider1tobeadded=64;
    		table_loaded="false"
    		groessentabelle()

    ///////////
    //  DOM  //
    ///////////
    var slideGroup = document.createElement('div');
    container.appendChild(slideGroup);
    slideGroup.style.position = 'relative';
    slideGroup.style.width =
    slideGroup.style.height =
        '100%';
    
    var slideBar = document.createElement('div');
    slideGroup.appendChild(slideBar);
    slideBar.style.position = 'absolute';
    slideBar.style.backgroundColor = '#000000';
        slideBar.style.height ="1px"

    slideBar.style.left =
    slideBar.style.right =
    slideBar.style.top ="15px"
    slideBar.style.bottom =
        Math.round(container.offsetHeight / 2 - 1) + 'px';
    
    
    
    var slideButton = document.createElement('div');
    slideGroup.appendChild(slideButton);
    slideButton.style.position = 'absolute';
    
    slideButton.style.width ="30px"
    slideButton.style.height ="30px"
    slideButton.style.borderRadius ="50%";
    slideButton.style.backgroundColor = '#000000';

    
    var colorAt = function(position) {
        
			zahl=position*100*slider1ratio+slider1tobeadded
        	slideButton.innerHTML=zahl.toFixed()
        	zahl=zahl.toFixed()
            
        //	document.getElementsByClassName("test")[0].innerHTML =zahl-63
        	if((zahl-63)>=0 && table_loaded=="true")
        	{

    			
        	    set_new_ratios_2(0.24,parseInt(groessentabelle_uebersicht[zahl-63][1]));
        	    
        	 
        	    
        	    //alert(groessentabelle_uebersicht[0][0])
        	}
        	



        return "#DB7093";
    };
    
    /////////////
    //  VALUE  //
    /////////////
    var value = null;
    
    slider.getValue = function() {
        return value;
    };
    
    slider.setValue = function(newValue) {

        value = Math.max(minValue, Math.min(maxValue, newValue));
       
        var position = (value - minValue) / (maxValue - minValue);
        
        slideButton.style.left = Math.round(position * slideBar.offsetWidth) + 'px';
         
        slideButton.style.backgroundColor = colorAt(position);


        slideButton.style.color = "#ffffff";
        
        slideButton.style.cursor = "pointer";
        slideButton.style.textAlign = "center";
        slideButton.style.lineHeight = "30px";
        
        
        
        
        if (slider.onChange) slider.onChange(value);
    };
    
    slider.setValue(minValue);
    
    /////////////
    //  MOUSE  //
    /////////////
    var sliding = false;
    var startX = 0;


    document.addEventListener('touchstart', function(event) {
        if (event.target === slideButton) {
            event.preventDefault();
            sliding = true;
            startX = event.pageX;
        }
    });
    
        document.addEventListener('touchend', function(event) {
        if (sliding) {
            sliding = false;
            startX = null;
        }
    });
    
        
    document.addEventListener('mousedown', function(event) {
        if (event.target === slideButton) {
            event.preventDefault();
            sliding = true;
            startX = event.pageX;
        }
    });
    
    
    
    document.addEventListener('mouseup', function(event) {
        if (sliding) {
            sliding = false;
            startX = null;
        }
    });
    
    document.addEventListener('mousemove', function(event) {
        if (sliding) {
            
            var newValue = value + ((event.pageX - startX) / slideBar.offsetWidth) * (maxValue - minValue);
            startX = event.pageX;

            
            slider.setValue(newValue);
            
        }
    });
    
    document.addEventListener('touchmove', function(event) {

        if (sliding) {
   
   
            var newValue = value + ((event.pageX - startX) / slideBar.offsetWidth) * (maxValue - minValue);
            startX = event.pageX;
            slider.setValue(newValue);
        }
    });
}


function set_new_ratios_1(ratio,tobeadded)
{


	    slider1ratio=ratio;
    	slider1tobeadded=tobeadded;

    	slider.setValue(100);

    //	test_.innerHTML=zahl.toFixed()
    	
}





function groesse_übernehmen()
{
    
	string_bh=document.getElementById("bh_groesse").innerHTML 
	string_bralette=document.getElementById("bralette_groesse").innerHTML 

	string_bh=string_bh.substr(string_bh.length - 3);
	if(string_bralette.length==26)
	    string_bralette=string_bralette.substr(string_bralette.length - 1);
	else
	    string_bralette=string_bralette.substr(string_bralette.length - 2);
	

	
	

	while(i<=sizes.length-1)
	{
	    

	    if(sizes[i].size==string_bh && sizes[i].type=="BH")
	        document.getElementsByClassName('bra_size_select')[0].value = string_bh
	    if(sizes[i].size=="Bralette "+string_bralette && sizes[i].type=="BH")
	        document.getElementsByClassName('bra_size_select')[0].value = "Bralette "+string_bralette	 
	        
	    i=i+1;       
	}
	
	$('#myModal').modal('toggle');

	



}

