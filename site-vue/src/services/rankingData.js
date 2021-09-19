import axios from 'axios'

// const mockData = {
//   rankings: [
//     {
//       site: 'greycastle.se',
//       keyword: 'greycastle flutter',
//       lastRanking: 1,
//       lastConfirmed: new Date(),
//       rankingsTotal: 12
//     }
//   ],
//   account: {
//     ranksTotal: 23,
//     ranksRemaining: 7,
//     rankSchedule: 3
//   }
// }

const mapResult = (result) => {
  const rankings = result.items.map((item) => ({
    downloadId: item.downloadId,
    keyword: item.keyword,
    site: item.site,
    lastRanking: item.lastRanking,
    rankingsTotal: item.rankings,
    lastConfirmed: Date.parse(item.lastConfirmed)
  }))

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

export default getRankingData;