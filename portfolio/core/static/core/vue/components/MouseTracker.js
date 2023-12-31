function useMouse() {
  const x = Vue.ref(0);
  const y = Vue.ref(0);

  function update(event) {
    x.value = event.pageX;
    y.value = event.pageY;
  }

  Vue.onMounted(() => window.addEventListener("mousemove", update));
  Vue.onUnmounted(() => window.removeEventListener("mousemove", update));

  return { x, y };
}

const MouseTracker = Vue.defineComponent({
  template: `
    <div class="mouse-tracker">
      Mouse position: {{ x }}, {{ y }}
    </div>
  `,
  setup() {
    const { x, y } = useMouse();
    return { x, y };
  },
});

window.MouseTracker = MouseTracker;
