const ProjectCard = Vue.defineComponent({
  template: `
    <img class="cover-image" :src="project.image_url" />
    <div class="card-details">
      <div class="title-row">
        <div class="companion">{{ project.title }}</div>
        <div class="price">$ 1,000,000</div>
      </div>
      <div class="description">{{ project.description.slice(0, 125) }}...</div>
      <div class="date-row">
        <div class="date">{{ project.start_date }} to {{ project.end_date || 'Ongoing' }}</div>
      </div>
    </div>
  `,
  props: {
    project: Object,
  },
});

window.ProjectCard = ProjectCard;
