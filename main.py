import downloadRuns
import generateRunnerProfiles
import generateLeaderboards
import calculateABRA

downloadRuns.getRuns()
generateRunnerProfiles.pullRunners(500)
generateLeaderboards.generate()
calculateABRA.calculate()