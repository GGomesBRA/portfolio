const ProjectCard = Vue.defineComponent({
  template: `
    <div class="project-card">
      <img class="cover-image" :src="project.image_url" />
      <div class="card-details">
        <div class="title-row">
          <div class="text-wrapper">{{ project.title }}</div>
          <div class="element">$ 1,000,000</div>
        </div>
        <p class="div">
          {{ project.description.slice(0, 125) }}...
        </p>
        <div class="date-row">
          <div class="text-wrapper-2">{{ project.start_date }} to {{ project.end_date || 'Ongoing' }}</div>
        </div>
      </div>
    </div>
  `,
  props: {
    project: Object,
  },
});

window.ProjectCard = ProjectCard;
