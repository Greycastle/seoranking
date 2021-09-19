import axios from 'axios'

const addRanking = async (site, keyword) => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/add_ranking_endpoint'
  try {
    await axios.post(url, {
      'rank_site': site,
      'keyword': keyword
    })
  } catch (err) {
    console.error(`Ran into an issue whilst getting '${url}': ${err}`)
    throw err
  }
}

export default addRanking;