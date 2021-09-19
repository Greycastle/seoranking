<template>
  <div class="container">
    <section class="header">
      <h2 class="title">About Ranking</h2>
      <p>
          SEO Ranking was built to provide an alternative to <b>SEMRUSH</b> or <b>SERanking</b>.
      </p>
      <p>
        Why do we need this tool? Because as a startup or a private blogger you don't need all the tools these other services provide. You only need to check how your ranking changes every few days and it might be worth a bit to you, if it works out, maybe a bit more but never $10/month. With this tool I hope to provide a cheaper alternative. That's it!
      </p>
      <p>
        It's completely free to get started! <br/>
        <router-link :to="{ name: 'Top' }" class="button button-primary">Check your ranking now</router-link>
      </p>
    </section>

    <Footer/>
  </div>
</template>
