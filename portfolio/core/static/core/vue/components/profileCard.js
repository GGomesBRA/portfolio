const ProfileCard = Vue.defineComponent({
  template: `
    <section class="main">
      <div class="profile-card">
        <div class="image">
          <img :src="profilePicture" alt="profile picture" class="profile-pic">
        </div>
        <div class="data">
          <h2>{{ name }}</h2>
          <h3>{{ role }}</h3>
          <span>{{ description }}</span>
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

window.ProfileCard = ProfileCard;
