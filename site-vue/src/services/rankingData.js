import axios from 'axios'

const mapRankingItems = (items) => {
  return items.map((item) => ({
    downloadId: item.downloadId,
    keyword: item.keyword,
    site: item.site,
    lastRanking: item.lastRanking,
    rankingsTotal: item.rankings,
    lastConfirmed: Date.parse(item.lastConfirmed)
  }))
}

const mapResult = (result) => {
  const rankings = mapRankingItems(result.items)

  const stats = result.stats;
  const account = {
    ranksTotal: stats.creditsSpent,
    ranksRemaining: stats.creditsLeft,
    rankSchedule: stats.schedule
  }

  return {
    rankings,
    account
  }
}

const getRankingData = async () => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/get_stats'
  try {
    const response = await axios.get(url)
    return mapResult(response.data)
  } catch (err) {
    console.error(`Ran into an issue whilst getting '${url}': ${err}`)
    throw err
  }
}

const getPublicRankings = async (id) => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/get_public_stats'
  const response = await axios.get(`${url}?id=${id}`)
  return mapRankingItems(response.data.items)
}

export {
  getRankingData,
  getPublicRankings
};