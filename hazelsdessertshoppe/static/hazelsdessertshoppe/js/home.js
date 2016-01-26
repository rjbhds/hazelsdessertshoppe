/*
Created using...
http://www.jssor.com/demos/full-width-slider.slider
*/
jQuery(document).ready(function ($) {
    
    var jssor_1_SlideoTransitions = [
      [{b:0,d:1000,x:850},{b:2600,d:600,x:150,y:80,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:400,d:800,x:750},{b:2800,d:600,x:50,y:-20,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:800,d:800,x:750},{b:3000,d:600,x:50,y:-80,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:1200,d:800,x:750},{b:3200,d:600,x:50,y:-140,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:1600,d:800,x:810},{b:3400,d:600,x:50,y:-200,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:300,y:310,o:1,r:360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:300,y:-233,o:1,r:-360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:-300,y:297,o:1,r:360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:-300,y:-235,o:1,r:-360,e:{r:4}}],
      [{b:0,d:1000,x:850},{b:2600,d:600,x:150,y:80,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:400,d:800,x:750},{b:2800,d:600,x:50,y:-20,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:800,d:800,x:750},{b:3000,d:600,x:50,y:-80,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:1200,d:800,x:750},{b:3200,d:600,x:50,y:-140,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:1600,d:800,x:810},{b:3400,d:600,x:50,y:-200,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:300,y:300,o:1,r:360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:300,y:-218,o:1,r:-360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:-300,y:254,o:1,r:360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:-300,y:-241,o:1,r:-360,e:{r:4}}],
      [{b:0,d:1000,x:850},{b:2600,d:600,x:150,y:80,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:400,d:800,x:750},{b:2800,d:600,x:50,y:-20,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:800,d:800,x:750},{b:3000,d:600,x:50,y:-80,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:1200,d:800,x:750},{b:3200,d:600,x:50,y:-140,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:1600,d:800,x:810},{b:3400,d:600,x:50,y:-200,o:-1,r:30,sX:9,sY:9,e:{x:2,y:6,r:1,sX:5,sY:5}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:300,y:152,o:1,r:360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:300,y:-351,o:1,r:-360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:-300,y:260,o:1,r:360,e:{r:4}}],
      [{b:-1,d:1,o:-1},{b:0,d:400,x:-300,y:-300,o:1,r:-360,e:{r:4}}]
    ];
    
    var jssor_1_options = {
      $AutoPlay: true,
      $Idle: 2000,
      $PauseOnHover: 3,
      $CaptionSliderOptions: {
        $Class: $JssorCaptionSlideo$,
        $Transitions: jssor_1_SlideoTransitions,
        $Breaks: [
          [{d:1000,b:2500}],
          [{d:1000,b:2500}],
          [{d:1000,b:2500}]
        ]
      },
      $ArrowNavigatorOptions: {
        $Class: $JssorArrowNavigator$
      },
      $BulletNavigatorOptions: {
        $Class: $JssorBulletNavigator$
      }
    };
    
    var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);
    
    //responsive code begin
    //you can remove responsive code if you don't want the slider scales while window resizing
    function ScaleSlider() {
        var refSize = jssor_1_slider.$Elmt.parentNode.clientWidth;
        if (refSize) {
            refSize = Math.min(refSize, 2000);
            jssor_1_slider.$ScaleWidth(refSize);
        }
        else {
            window.setTimeout(ScaleSlider, 30);
        }
    }
    ScaleSlider();
    $(window).bind("load", ScaleSlider);
    $(window).bind("resize", ScaleSlider);
    $(window).bind("orientationchange", ScaleSlider);
    //responsive code end
});
