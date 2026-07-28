/* =====================================================
   MemoryVerse AI
   Premium Animation Engine
===================================================== */

// Initialize AOS
AOS.init({
    duration: 1000,
    easing: "ease-in-out",
    once: true,
    offset: 80
});

// Register GSAP Plugin
gsap.registerPlugin(ScrollTrigger);

/* ==========================================
   Hero Entrance Animation
========================================== */

const heroTimeline = gsap.timeline();

heroTimeline
.from(".navbar", {
    y: -80,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
})

.from(".hero-content h1", {
    y: 80,
    opacity: 0,
    duration: 1,
    ease: "power4.out"
}, "-=0.4")

.from(".hero-content p", {
    y: 40,
    opacity: 0,
    duration: 0.8
}, "-=0.6")

.from(".hero-buttons", {
    y: 40,
    opacity: 0,
    duration: 0.8
}, "-=0.5")

.from(".hero-users", {
    y: 40,
    opacity: 0,
    duration: 0.8
}, "-=0.5")

.from(".brain-container", {
    scale: 0.5,
    opacity: 0,
    rotate: -15,
    duration: 1.2,
    ease: "back.out(1.7)"
}, "-=0.8");

/* ==========================================
   Floating Brain Animation
========================================== */

gsap.to(".brain-container", {

    y: -18,

    duration: 3,

    repeat: -1,

    yoyo: true,

    ease: "sine.inOut"

});

/* ==========================================
   Floating Nodes
========================================== */

gsap.to(".node", {

    y: -10,

    stagger: 0.2,

    duration: 2,

    repeat: -1,

    yoyo: true,

    ease: "sine.inOut"

});

/* ==========================================
   Feature Cards Animation
========================================== */

gsap.from(".feature-card", {

    scrollTrigger: {

        trigger: ".features",

        start: "top 75%"

    },

    y: 80,

    opacity: 0,

    duration: 1,

    stagger: 0.2,

    ease: "power3.out"

});

/* ==========================================
   Workflow Animation
========================================== */

gsap.from(".workflow-step", {

    scrollTrigger: {

        trigger: ".workflow",

        start: "top 75%"

    },

    scale: 0.8,

    opacity: 0,

    duration: 0.8,

    stagger: 0.2

});

/* ==========================================
   Statistics Animation
========================================== */

gsap.from(".stat-card", {

    scrollTrigger: {

        trigger: ".stats",

        start: "top 75%"

    },

    y: 60,

    opacity: 0,

    duration: 0.8,

    stagger: 0.15

});