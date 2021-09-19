import axios from 'axios'

const addRanking = async (site, keyword) => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/add_ranking_endpoint'
  await axios.post(url, {
    'rank_site': site,
    'keyword': keyword
  })
}

export default addRanking;