new Vue({
  el: "#app",
  data: {
    newTask: "",
    tasks: ["Task 1", "Task 2"],
  },
  methods: {
    addTask() {
      if (this.newTask !== "") {
        this.tasks.push(this.newTask);
        this.newTask = "";
      }
    },
  },
});
