class Args:
    ySubmitLogName = 'ySubmit.log'
    fileList = '/star/u/yghuang/Work/DataAnalysis/BES2/11p5/cqa/1GetList/file.list'
    jobPath = '/star/u/yghuang/pwgdata/DataAnalysis/BES2/11p5/yqa/qaDst'
    # ==========================
    # run mode settings
    runNumberList = '/star/u/yghuang/Work/DataAnalysis/BES2/11p5/cqa/1GetList/run.list'
    runNumberLoc = 9
    # ==========================
    # normal mode settings
    nFilesPerJob = 20
    # ==========================
    # merge mode settings
    nJobs = 50
    mergePath = './merge/'
    # ==========================
    # copy or symlink packages
    lnsList = [
        'StRoot',
        '.sl73_gcc485',
    ]
    cprList = [

    ]
    cpList = [
        'readPicoDst.C',
        'run.sh'
    ]
    
