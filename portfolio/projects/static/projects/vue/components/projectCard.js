const ProjectCard = Vue.defineComponent({
  template: `
    <div class="card">
        <img class="card-img-top" :src="project.image_url" alt="Card image cap" style="width: 100%; height: 200px; object-fit: cover;">
      <div class="card-body">
        <h5 class="card-title">{{ project.title }} {{project.image_url}} </h5>
        <p class="card-text">{{ project.start_date }} - {{ project.end_date || 'Ongoing' }}</p>
        <p class="card-text">{{ project.description }}...</p>
      </div>
    </div>
  `,
  props: {
    project: Object,
  },
});

window.ProjectCard = ProjectCard;
