import axios from 'axios'

const register = async (email, keyword, site) => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/register';
  const query = `?query=${encodeURIComponent(keyword)}&rank_site=${encodeURIComponent(site)}&user=${encodeURIComponent(email)}`
  await axios.post(url + query)
}

export default register;