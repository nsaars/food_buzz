(function($){
    "use strict";
    $(window).on('load', function(){
		$('.preloader').fadeOut(1000);
    })
    
    // lightcase 
    $('a[data-rel^=lightcase]').lightcase();

    // mobile shop responsive
    $(document).on('click','.header-bar',function(){
        $(".header-bar").toggleClass("close");
        $(".mobile-shop").toggleClass("open");
    });

    // Header Section Menu Part
    $(".main-shop ul li ul, .mobile-shop-area-inner ul li ul").parent("li").addClass("menu-item-has-children");

    //mobile drodown shop display
    $('.shop-item-has-children>a').on('click', function(e){
        event.preventDefault();
    });
    $('.mobile-shop-area ul li a, .shop-shop li a').on('click', function(e) {
        var element = $(this).parent('li');
        if (element.hasClass('open')) {
            element.removeClass('open');
            element.find('li').removeClass('open');
            element.find('ul').slideUp(1000,"swing");
        }
        else {
            element.addClass('open');
            element.children('ul').slideDown(1000,"swing");
            element.siblings('li').children('ul').slideUp(1000,"swing");
            element.siblings('li').removeClass('open');
            element.siblings('li').find('li').removeClass('open');
            element.siblings('li').find('ul').slideUp(1000,"swing");
        }
    });

    // drop down shop width overflow problem fix
    $('ul').parent().on("hover", function() {
        var menu = $(this).find("ul");
        var menupos = $(menu).offset();
        if (menupos.left + menu.width() > $(window).width()) {
            var newpos = -$(menu).width();
            menu.css({ left: newpos });    
        }
    });


    // scroll up start here
    $(function(){
        $(window).scroll(function(){
            if ($(this).scrollTop() > 300) {
                $('.scrollToTop').css({'bottom':'10%', 'opacity':'1','transition':'all .5s ease'});
            } else {
                $('.scrollToTop').css({'bottom':'-30%', 'opacity':'0','transition':'all .5s ease'})
            }
        });
        //Click event to scroll to top
        $('.scrollToTop').on('click', function(){
            $('html, body').animate({scrollTop : 0},500);
            return false;
        });
    });

    
    // product view mode change js
    $(function() {
        $('.product-view-mode').on('click', 'a', function (e) {
            e.preventDefault();
            var shopProductWrap = $('.shop-product-wrap');
            var viewMode = $(this).data('target');
            $('.product-view-mode a').removeClass('active');
            $(this).addClass('active');
            shopProductWrap.removeClass('grid list').addClass(viewMode);
        });
    });

    // search 
    $(document).on('click','.search, .search-close',function(){
        $(".search-area").toggleClass("open");
    });
    // cart option
    $(document).on('click','.cart-icon, .list-close',function(){
        $(".cart-area").toggleClass("open");
    });

    // sponsor slider section
    var swiper = new Swiper('.sponsor-slider', {
        slidesPerView: 6,
        spaceBetween: 10,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        breakpoints: {
            992: {
                slidesPerView: 3,
            },
            576: {
                slidesPerView: 2,
            },
            420: {
                slidesPerView: 1,
            },
        },
        loop: true,
    });


    // food slider section
    var swiper = new Swiper('.post-thumb-slider', {
        slidesPerView: 1,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: '.post-thumb-slider-next',
            prevEl: '.post-thumb-slider-prev',
        },
        loop: true,
    });





    // shop cart + - start here
    $(".qtybutton").on("click", function() {
        let oldValue = parseInt($(this).parent().find("input").val());
        let newValue;
        let operation;
        if ($(this).text() === "+" || oldValue > 1) {
                operation = $(this).text() === "+" ? 1 : -1;
                newValue = oldValue + operation;

                $(this).parent().find("input").val(newValue);
                let productPrice =  $(this).parentsUntil('.cart-product').last().parent().find('.product-price').text();

                let $productTotalSection = $(this).parentsUntil('.cart-product').last().parent().find('.product-total');
                let productTotal = newValue * productPrice;
                $productTotalSection.text(productTotal);

                let $cartTotalSection = document.getElementsByClassName('cart-total')[0];
                $cartTotalSection.textContent = (parseInt($cartTotalSection.textContent) + productPrice * operation).toString();

                let $orderTotalSection = document.getElementsByClassName('order-total')[0];
                $orderTotalSection.textContent = (parseInt($orderTotalSection.textContent) + productPrice * operation).toString();

                let productTitle = $(this).parentsUntil('.cart-product').last().parent().find('.product-title').text()

                $.ajax({
                    url: 'change-quantity',
                    data: {product_title: productTitle, quantity: newValue, cart_total: parseInt($cartTotalSection.textContent), order_total: parseInt($orderTotalSection.textContent)},
                    success: function(response){
                        console.log(response);
                    }
                })
        }

    });


    $(".city-select").on( 'change', function (){
        let $citySelect = $(this);
        let cityId = parseInt($citySelect.val());

        $.ajax({
            url: 'change-city',
            data: {city_id: cityId},
            success: function(response){
                let $shippingPriceSection = $citySelect.parentsUntil('.row').last().parent().find('.shiping-price');
                $shippingPriceSection.text(response.shippingPrice);

                let $orderTotalSection = $citySelect.parentsUntil('.row').last().parent().find('.order-total');
                $orderTotalSection.text(response.orderTotal);
            }
        })


    });



    $(".food-btn").on('click', function () {
        let $foodButton = $(this);
        let quantity = $foodButton.parent().find('.quantity').val();
        if (quantity){
            let url = window.location.pathname;
            let parts = url.split('/');
            let productSlug = parts[parts.length-2];
            $.ajax({
                url: '/cart/add-to-cart/',
                data: {product_slug: productSlug, quantity: quantity},
                success: function (response) {
                    window.location.replace(response);
                }
            })
        }
    });

    $(".food-btn-2").on('click', function () {
        let $foodButton = $(this);
        $foodButton.parent().css('background-color', 'green');
        let productSlug = $foodButton.attr('id');
        $.ajax({
            url: '/cart/add-to-cart/',
            data: {product_slug: productSlug},
            success: function (response) {
                $foodButton.parent().attr('href', response);
            }
        })
    });

    $(".remove-button").on('click', function () {
        let $removeButton = $(this);
        let $product = $removeButton.parentsUntil('.cart-product').last().parent();
        let productTitle = $product.find('.product-title').text()
        $.ajax({
            url: '/cart/remove-from-cart/',
            data: {product_title: productTitle},
            success: function (response) {
                $product.remove();

                let $cartTotalSection = document.getElementsByClassName('cart-total')[0];
                $cartTotalSection.textContent = (parseInt($cartTotalSection.textContent) - response.totalProductPrice).toString();

                let $orderTotalSection = document.getElementsByClassName('order-total')[0];
                $orderTotalSection.textContent = (parseInt($orderTotalSection.textContent) - response.totalProductPrice).toString();

                if (response.cartLength === 0){
                    let $orderButton = document.getElementsByClassName('cart-checkout-box')[0];
                    $orderButton.remove();
                }
            }
        })
    });

    $(".pvm-1, .pvm-2").on('click', function (){
        let className = $(this).attr('class')
        console.log(className);
        $.ajax({
            url: 'change-view-mode/',
            data: {pvm: className},
        })
    })
    // banner slider
    var galleryThumbs = new Swiper('.gallery-thumbs', {
        spaceBetween: 10,
        slidesPerView: 4,
        freeMode: true,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
        breakpoints: {
			768: {
				slidesPerView: 3,
            },
            576: {
				slidesPerView: 2,
            },
            450: {
				slidesPerView: 1,
            }
		}
    });
    var galleryTop = new Swiper('.gallery-top', {
        spaceBetween: 10,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        thumbs: {
            swiper: galleryThumbs
        },
        loop: true,
    });

    // testimonoial
    var galleryThumbs = new Swiper('.testi-thumbs', {
        spaceBetween: 20,
        slidesPerView: 1,
        freeMode: true,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
        loop: true
    });
    var galleryTop = new Swiper('.testi-top', {
        spaceBetween: 0,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        thumbs: {
            swiper: galleryThumbs
        },
        loop: true
    });



    /*---clients slider activation---*/
	var swiper = new Swiper('.clients-container', {
		slidesPerView: 1,
		speed:1000,
		// autoplay: true,
		loop: true,
		// freeMode: true,
		// autoplay: {
        //     delay: 2000,
        //     disableOnInteraction: false,
        // },
		pagination: {
			el: '.clients-pagination',
			clickable: true,
		},
		breakpoints: {
			1024: {
				slidesPerView: 1,
			},
			767: {
				slidesPerView: 1,
			}
		}
    });
    
    // skill 
    $(window).scroll(function() {
        // skill bar or progress bar
        var skillLevel1 = jQuery('.first').data('percent');
        $('.first.circle').circleProgress({
            value:  '0.' + skillLevel1,
            fill: {gradient: ['#2dca73']}
        }).on('circle-animation-progress', function(event, progress) {
            $(this).find('strong').html(Math.round(skillLevel1 * progress) + '<i>%</i>');
        });
        //Circle ProgressBarTwo
        var skillLevel2 = jQuery('.second').data('percent');
        $('.second.circle').circleProgress({
            value:  '0.' + skillLevel2,
            fill: {gradient: ['#ff7d51']}
        }).on('circle-animation-progress', function(event, progress) {
            $(this).find('strong').html(Math.round(skillLevel2 * progress) + '<i>%</i>');
        });
        //Circle ProgressBarThree
        var skillLevel3 = jQuery('.third').data('percent');
        $('.third.circle').circleProgress({
            value:  '0.' + skillLevel3,
            fill: {gradient: ['#ffc212']}
        }).on('circle-animation-progress', function(event, progress) {
            $(this).find('strong').html(Math.round(skillLevel3 * progress) + '<i>%</i>');
        });
    });


    // Ajax Style start here
    $('.load-more').on('click', function(e) {
        e.preventDefault();
        var $self = $(e.currentTarget),
            $container = $self.closest('.rajib');
        
        // don't allow another load when already loading
        if($self.hasClass('loading')) {
          return;
        }
        $self.addClass('loading');

        var item = ['<div class="col-lg-6 col-12"><div class="product-item style-2"><div class="product-thumb"> <img src="assets/images/product/01.jpg" alt="food-product"><span class="price">$20</span></div><div class="product-content"><div class="product-title"><h6><a href="#">Cream Chicken Chiladas</a></h6><div class="rating"><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i></div></div><div class="product-desc"><p>Conveniently imaiipact are worldwide andng datang arovem theme with there</p></div> </div></div></div><div class="col-lg-6 col-12"><div class="product-item style-2"><div class="product-thumb"> <img src="assets/images/product/02.jpg" alt="food-product"><span class="price">$20</span></div><div class="product-content"><div class="product-title"><h6><a href="#">Cream Chicken Chiladas</a></h6><div class="rating"><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i></div></div><div class="product-desc"><p>Conveniently imaiipact are worldwide andng datang arovem theme with there</p></div> </div></div></div><div class="col-lg-6 col-12"><div class="product-item style-2"><div class="product-thumb"> <img src="assets/images/product/03.jpg" alt="food-product"><span class="price">$20</span></div><div class="product-content"><div class="product-title"><h6><a href="#">Cream Chicken Chiladas</a></h6><div class="rating"><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i></div></div><div class="product-desc"><p>Conveniently imaiipact are worldwide andng datang arovem theme with there</p></div> </div></div></div>'],
        
        items = '',
        itemsPerRow = 2;
    
        for (var i = 0; i < itemsPerRow; i++) {  
            items += item;
        }
        
        var $newrow = $(items);
        
        // timeout delay values
        var ajaxDelay = 2000,
            animationWait = 50,
            animationDuration = 201;
      
        // mimic ajax call
        setTimeout(function() {
          $newrow.insertBefore($self);
          // delay to show intro animation
          setTimeout(function() {
            $newrow.removeClass('intro-animation');
            // delay to return all back to their default state
            setTimeout(function() {
              $self.removeClass('loading');
              $newrow.removeClass('ajax');
            }, animationDuration);
          }, animationWait);
        }, ajaxDelay);
        
    }); // END click handler

    // Ajax Style 2 start here
    $('.load-more-2').on('click', function(e) {
        e.preventDefault();
        var $self = $(e.currentTarget),
            $container = $self.closest('.rajib');
        
        // don't allow another load when already loading
        if($self.hasClass('loading')) {
          return;
        }
        $self.addClass('loading');
        
        var item = ['<div class="col-xl-3 col-md-6 col-12"><div class="product-item"><div class="product-thumb"> <img src="assets/images/product/01.jpg" alt="food-product"><span class="price">$20</span></div><div class="product-content"><div class="product-title"><h6><a href="#">Cream Chicken Chiladas</a></h6><div class="rating"><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i></div></div></div></div></div><div class="col-xl-3 col-md-6 col-12"><div class="product-item"><div class="product-thumb"> <img src="assets/images/product/02.jpg" alt="food-product"><span class="price">$20</span></div><div class="product-content"><div class="product-title"><h6><a href="#">Cream Chicken Chiladas</a></h6><div class="rating"><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i><i class="icofont-star"></i></div></div></div></div></div>'],

        items = '',
        itemsPerRow = 2;
    
        for (var i = 0; i < itemsPerRow; i++) {
            items += item;
        }
        
        var $newrow = $(items);
        
        // timeout delay values
        var ajaxDelay = 2000,
            animationWait = 50,
            animationDuration = 201;
      
        // mimic ajax call
        setTimeout(function() {
          $newrow.insertBefore($self);
          // delay to show intro animation
          setTimeout(function() {
            $newrow.removeClass('intro-animation');
            // delay to return all back to their default state
            setTimeout(function() {
              $self.removeClass('loading');
              $newrow.removeClass('ajax');
            }, animationDuration);
          }, animationWait);
        }, ajaxDelay);
        
    }); // END click handler

    $('.internal-link').on('click', function() {
       var scrollName = $(this).attr('href'),
           scrollElem = $(scrollName),
           scrollTop = scrollElem.offset().top;

       $('html, body').animate({
          scrollTop: scrollTop
       }, 500);
       return false;
    });

}(jQuery));