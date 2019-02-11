var slider2ratio;
var slider2tobeadded;
var position;
var zahl2;
var ratio_;

var slider1ratio;
var slider1tobeadded;
var zahl;
var table_loaded;



var slider2 = new slider2(document.getElementById('slider2'),75, 99);
slider2.onChange = function(value) {
     
    //document.getElementById('value').textContent = Math.round(value);
};


function slider2(container, minValue, maxValue) {
    var slider2 = this;
    		slider2ratio=0.24;
    		slider2tobeadded=75;
    		ratio_=0.83
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
        slideBar.style.top ="15px"
        slideBar.style.backgroundColor = '#000000';
                slideBar.style.height ="1px"

    slideBar.style.left =
    slideBar.style.right =

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
    		
			zahl2=position*100*slider2ratio+slider2tobeadded
        	slideButton.innerHTML=zahl2.toFixed()
        	zahl2=zahl2.toFixed()

        	
        	if((zahl-63)>=0 && zahl2-slider2tobeadded>=0 && table_loaded=="true" )
        	{
        	    

        	  	if(groessentabelle_detailliert[zahl-63][1][zahl2-slider2tobeadded]!="")
        	        document.getElementsByClassName("headline_overlay")[0].innerHTML ="<div id='bh_groesse'>Deine BH-Größe ist "+groessentabelle_detailliert[zahl-63][0][zahl2-slider2tobeadded]+"</div><div id='bralette_groesse' style='font-size:14px'>Deine Bralette-Größe ist "+groessentabelle_detailliert[zahl-63][1][zahl2-slider2tobeadded]+"</div>"
                else
        	        document.getElementsByClassName("headline_overlay")[0].innerHTML ="<div id='bh_groesse'>Deine BH-Größe ist "+groessentabelle_detailliert[zahl-63][0][zahl2-slider2tobeadded]+"</div><div id='bralette_groesse' style='font-size:14px'>&nbsp;</div>"
        	    check_sizing(groessentabelle_detailliert[zahl-63][0][zahl2-slider2tobeadded],groessentabelle_detailliert[zahl-63][1][zahl2-slider2tobeadded])
        	     document.getElementsByClassName("slider_text_anfang_links")[1].innerHTML =groessentabelle_uebersicht[zahl-63][1]
        	      document.getElementsByClassName("slider_text_anfang_rechts")[1].innerHTML =groessentabelle_uebersicht[zahl-63][2]


        	     
        	    
        	}
        	else
        	    slideButton.innerHTML="95"





        return "#CC3366";
    };
    
    /////////////
    //  VALUE  //
    /////////////
    var value = null;
    
    slider2.getValue = function() {
        return value;
    };
    
    slider2.setValue = function(newValue) {

        value = Math.max(minValue, Math.min(maxValue, newValue));
        var position = (value - minValue) / (maxValue - minValue);
        
        slideButton.style.left = Math.round(position * slideBar.offsetWidth) + 'px';

        slideButton.style.backgroundColor = colorAt(position);


        slideButton.style.color = "#ffffff";
        
        slideButton.style.cursor = "pointer";
        slideButton.style.textAlign = "center";
        slideButton.style.lineHeight = "30px";
        
        
      
        
        if (slider2.onChange) slider2.onChange(value);
          
    };
    
    slider2.setValue(minValue);
    
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
            slider2.setValue(newValue);
        }
    });
    
    document.addEventListener('touchmove', function(event) {

        if (sliding) {
   
   
            var newValue = value + ((event.pageX - startX) / slideBar.offsetWidth) * (maxValue - minValue);
            startX = event.pageX;
            slider2.setValue(newValue);
        }
    });
}


function set_new_ratios_2(ratio,tobeadded)
{

	    slider2ratio=ratio;

    	slider2tobeadded=tobeadded;

    	slider2.setValue(ratio_*100);
 
}

