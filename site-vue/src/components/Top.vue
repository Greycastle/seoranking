<template>
  <div class="container">
    <section class="header">
      <h2 class="title">SEO Ranking</h2>
      <p>
          This tool allows you to sign up for continous search ranking checks for your site.
      </p>
    </section>

    <div id="first-view">
      <div class="page-section">
        <h3>Get started</h3>
        <p>
            Enter your email to get reports to here and then your keyword and your site:
        </p>
        <form class="form">
          <div class="row">
              <p>
                  <label for="keyword">Keyword</label>
                  <input placeholder="yummy greens" class="remember-input u-full-width" type="text" id="keyword">

              </p>
              <p>
                <label for="site">Site</label>
                <input placeholder="greens.zed" class="remember-input u-full-width" type="text" id="site">
              </p>
              <p>
                <label for="api-key">Email</label>
                <input placeholder="sales@greens.zed" class="remember-input u-full-width" type="email" id="email">
              </p>
          </div>
          <p><button id="sign-up" class="button-primary" type="button">Check ranking!</button></p>
        </form>
      </div>

      <div class="page-section">
        <h3>Already started?</h3>
        <p>
            If you've already registered, log in to see your recent ranking history.
        </p>
        <p>
          <router-link class="button button-primary" to="'/login">Check your ranking history</router-link>
        </p>
      </div>
    </div>
    <div id="signed-up">
      <div class="page-section">
        <h3>Registered!</h3>
        <p>
            All set up! Welcome onboard! <br/>
            Give it a minute and we'll start checking your rank.
        </p>
        <p>
          <router-link class="button button-primary" to="'/login">Login to check your rank</router-link>
        </p>
      </div>
    </div>

    <div class="page-section">
      <h3>About</h3>
      <p>
          This app is built by <a target="_blank" href="https://twitter.com/almundgrey">David</a> @ <a target="_blank" href="https://greycastle.se">Greycastle</a>, visuals based on the <a target="_blank" href="http://getskeleton.com/">Skeleton</a> css framework. <a href="about.html">About</a> | <a href="pricing.html">Pricing</a>.
      </p>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
</style>