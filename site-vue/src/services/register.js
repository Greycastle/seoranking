import axios from 'axios'

const register = async (email, keyword, site) => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/register';
  try {
    const query = `?query=${encodeURIComponent(keyword)}&rank_site=${encodeURIComponent(site)}&user=${encodeURIComponent(email)}`
    await axios.post(url + query)
  } catch (err) {
    console.error(`Ran into an issue whilst getting '${url}': ${err}`)
    throw err
  }
}

export default register;