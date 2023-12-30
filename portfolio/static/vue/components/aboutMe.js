Vue.component("about-me-card", {
  template: `
    <div class="row">
      <div class="col" v-for="profile in profiles">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ profile.title }}</h5>
            <p class="card-text">Name: {{ profile.name }}</p>
            <p class="card-text">Age: {{ profile.age }}</p>
            <p class="card-text">Years of Experience: {{ profile.yearsOfExperience }}</p>
            <p class="card-text">Tech Stack:</p>
            <ul>
              <li v-for="tech in profile.techStack">{{ tech }}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  `,
  data() {
    return {
      profiles: [
        {
          title: "About me",
          name: "GABRIEL",
          age: 30,
          yearsOfExperience: 5,
          techStack: ["Python", "Django", "Vue", "PostgreSQL"],
        },
        {
          title: "About me",
          name: "ALICE",
          age: 28,
          yearsOfExperience: 3,
          techStack: ["JavaScript", "React", "Node.js"],
        },
        {
          title: "About me",
          name: "BOB",
          age: 35,
          yearsOfExperience: 10,
          techStack: ["Java", "Spring", "Hibernate"],
        },
      ],
    };
  },
});

new Vue({ el: "#aboutMeCards" });
