import { getAnalytics, logEvent } from "firebase/analytics";

class Analytics {
  constructor(firebaseApp, router) {
    this.analytics = getAnalytics(firebaseApp);

    router.afterEach((to) => {
      logEvent(this.analytics, "page_view", { page_path: to.path, page_title: to.name });
    })

    logEvent(this.analytics, "page_view", { page_path: router.currentRoute.path, page_title: router.currentRoute.name });
  }
}

export default {
  install: (app, options) => {
    const router  = app.config.globalProperties.$router
    if (!router) {
      throw new Error("Please register router before the analytics module")
    }

    const analytics = new Analytics(options.firebaseApp, router)
    app.config.globalProperties.$analytics = analytics
  }
};