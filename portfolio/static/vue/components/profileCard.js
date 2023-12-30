Vue.component("profile-card", {
  template: `
  <section class="main">
    <div class="profile-card">
      <div class="image">
        <img :src="profilePicture" alt="profile picture" class="profile-pic">
      </div>
      <div class="data">
        <h2>{{ name }}</h2>
        <h3>{{ role }}</h3>
        <span>{{description}}</span>
      </div>
      <div class = "row">
        <div class="col">
          <div class="buttons">
            <a href="#" class="btn">Blog</a> 
          </div>
        </div>
        <div class="col">
          <div class="buttons">
            <a href="#" class="btn">Projects</a>
          </div>
        </div>
      </div>
    </div>
  </section>
  `,
  props: {
    name: String,
    role: String,
    description: String,
    profilePicture: String,
  },
});

new Vue({ el: "#profileCard" });
