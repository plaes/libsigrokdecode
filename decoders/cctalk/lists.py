standard_commands = {
    255: 'FactorySetup',
    254: 'SimplePoll',
    253: 'AddressPoll',
    252: 'AddressClash',
    251: 'AddressChange',
    250: 'AddressRandom',
    249: 'RequestPollingPriority',
    248: 'RequestStatus',
    247: 'RequestVariableSet',
    246: 'RequestManufacturerId',
    245: 'RequestEquipmentCategoryId',
    244: 'RequestProductCode',
    243: 'RequestDatabaseVersion',
    242: 'RequestSerialNumber',
    241: 'RequestSoftwareRevision',
    240: 'TestSolenoids',
    239: 'OperateMotors',
    238: 'TestOutputLines',
    237: 'ReadInputLines',
    236: 'ReadOptoStates',
    235: 'ReadLastCreditOrErrorCode',
    234: 'IssueGuardCode',
    233: 'LatchOutputLines',
    232: 'PerformSelfcheck',
    231: 'ModifyInhibitStatus',
    230: 'RequestInhibitStatus',
    229: 'ReadBufferedCreditOrErrorCodes',
    228: 'ModifyMasterInhibitStatus',
    227: 'RequestMasterInhibitStatus',
    226: 'RequestInsertionCounter',
    225: 'RequestAcceptCounter',
    224: 'DispenseCoins',
    223: 'DispenseChange',
    222: 'ModifySorterOverrideStatus',
    221: 'RequestSorterOverrideStatus',
    220: 'OneshotCredit',
    219: 'EnterNewPINNumber',
    218: 'EnterPINNumber',
    217: 'RequestPayoutHighLowStatus',
    216: 'RequestDataStorageAvailability',
    215: 'ReadDataBlock',
    214: 'WriteDataBlock',
    213: 'RequestOptionFlags',
    212: 'RequestCoinPosition',
    211: 'PowerManagementControl',
    210: 'ModifySorterPaths',
    209: 'RequestSorterPaths',
    208: 'ModifyPayoutAbsoluteCount',
    207: 'RequestPayoutAbsoluteCount',
    206: 'EmptyPayout',
    205: 'RequestAuditInformationBlock',
    204: 'MeterControl',
    203: 'DisplayControl',
    202: 'TeachModeControl',
    201: 'RequestTeachStatus',
    200: 'UploadCoinData',
    199: 'ConfigurationToEEPROM',
    198: 'CountersToEEPROM',
    197: 'CalculateROMChecksum',
    196: 'RequestCreationDate',
    195: 'RequestLastModificationDate',
    194: 'RequestRejectCounter',
    193: 'RequestFraudCounter',
    192: 'RequestBuildCode',
    191: 'KeypadControl',
    190: 'RequestPayoutStatus',
    189: 'ModifyDefaultSorterPath',
    188: 'RequestDefaultSorterPath',
    187: 'ModifyPayoutCapacity',
    186: 'RequestPayoutCapacity',
    185: 'ModifyCoinId',
    184: 'RequestCoinId',
    183: 'UploadWindowData',
    182: 'DownloadCalibrationInfo',
    181: 'ModifySecuritySetting',
    180: 'RequestSecuritySetting',
    179: 'ModifyBankSelect',
    178: 'RequestBankSelect',
    177: 'HandheldFunction',
    176: 'RequestAlarmCounter',
    175: 'ModifyPayoutFloat',
    174: 'RequestPayoutFloat',
    173: 'RequestThermistorReading',
    172: 'EmergencyStop',
    171: 'RequestHopperCoin',
    170: 'RequestBaseYear',
    169: 'RequestAddressMode',
    168: 'RequestHopperDispenseCount',
    167: 'DispenseHopperCoins',
    166: 'RequestHopperStatus',
    165: 'ModifyVariableSet',
    164: 'EnableHopper',
    163: 'TestHopper',
    162: 'ModifyInhibitAndOverrideRegisters',
    161: 'PumpRNG',
    160: 'RequestCipherKey',
    159: 'ReadBufferedBillEvents',
    158: 'ModifyBillId',
    157: 'RequestBillId',
    156: 'RequestCountryScalingFactor',
    155: 'RequestBillPosition',
    154: 'RouteBill',
    153: 'ModifyBillOperatingMode',
    152: 'RequestBillOperatingMode',
    151: 'TestLamps',
    150: 'RequestIndividualAcceptCounter',
    149: 'RequestIndividualErrorCounter',
    148: 'ReadOptoVoltages',
    147: 'PerformStackerCycle',
    146: 'OperateBidirectionalMotors',
    145: 'RequestCurrencyRevision',
    144: 'UploadBillTables',
    143: 'BeginBillTableUpgrade',
    142: 'FinishBillTableUpgrade',
    141: 'RequestFirmwareUpgradeCapability',
    140: 'UploadFirmware',
    139: 'BeginFirmwareUpgrade',
    138: 'FinishFirmwareUpgrade',
    137: 'SwitchEncryptionCode',
    136: 'StoreEncryptionCode',
    135: 'SetAcceptLimit',
    134: 'DispenseHopperValue',
    133: 'RequestHopperPollingValue',
    132: 'EmergencyStopValue',
    131: 'RequestHopperCoinValue',
    130: 'RequestIndexedHopperDispenseCount',
    129: 'ReadBarcodeData',
    128: 'RequestMoneyIn',
    127: 'RequestMoneyOut',
    126: 'ClearMoneyCounters',
    125: 'PayMoneyOut',
    124: 'VerifyMoneyOut',
    123: 'RequestActivityRegister',
    122: 'RequestErrorStatus',
    121: 'PurgeHopper',
    120: 'ModifyHopperBalance',
    119: 'RequestHopperBalance',
    118: 'ModifyCashboxValue',
    117: 'RequestCashboxValue',
    116: 'ModifyRealTimeClock',
    115: 'RequestRealTimeClock',
    114: 'RequestUSBId',
    113: 'SwitchBaudRate',
    112: 'ReadEncryptedEvents',
    111: 'RequestEncryptionSupport',
    110: 'SwitchEncryptionKey',
    109: 'RequestEncryptedHopperStatus',
    108: 'RequestEncryptedMonetaryId',
    4: 'RequestCommsRevision',
    3: 'ClearCommsStatusVariables',
    2: 'RequestCommsStatusVariables',
    1: 'ResetDevice',
    0: 'Reply',
}

