from dataclasses import dataclass
from typing import List
from typing import Union


#### Things ####
@dataclass
class JudicialEntity:
    Jurisdiction: str
    RegulatoryAuthority: str
    LegalSystem: str

@dataclass
class FinancialMarket:
    # properties
    name: str
    country: str
    currency: str
    timezone: str
    opening_time: str
    closing_time: str

@dataclass
class FinancialInstruments:
    # properties
    name: str
    annual_return: float
    risk: float
    issued_institution: JudicialEntity # TODO: modify to a subclass of JudicialEntity
    market: JudicialEntity # TODO: modify to a subclass of JudicialEntity, market where this financial instrument is traded

@dataclass
class GovernmentPolicy:
    pass

@dataclass
class MonetaryPolicy(GovernmentPolicy):
    pass

@dataclass
class FiscalPolicy(GovernmentPolicy):
    pass

@dataclass
class FinancialRegulation(GovernmentPolicy):
    pass

@dataclass
class FinancialInstitutions(JudicialEntity):
    pass

@dataclass
class Banks(FinancialInstitutions):
    pass

@dataclass
class SecuritiesFirms(FinancialInstitutions):
    pass

@dataclass
class InsuranceCompanies(FinancialInstitutions):
    pass

@dataclass
class CreditRatingAgency(FinancialInstitutions):
    pass

@dataclass
class Government(JudicialEntity):
    pass

@dataclass
class Regulators(JudicialEntity):
    pass

@dataclass
class StockExchange(FinancialMarket):
    pass

@dataclass
class BondMarket(FinancialMarket):
    pass

@dataclass
class MoneyMarket(FinancialMarket):
    pass

@dataclass
class ForeignExchangeMarket(FinancialMarket):
    pass

@dataclass
class CommodityMarket(FinancialMarket):
    pass

@dataclass
class CryptocurrencyMarket(FinancialMarket):
    pass

@dataclass
class FinancialInstrumentMarket(FinancialMarket):
    pass

@dataclass
class SecutityCompany():
    pass

@dataclass
class DebtInstrument(FinancialInstruments):
    # properties
    interest_rate: float
    issuer: SecutityCompany
    market: FinancialMarket

@dataclass
class EquityInstruments(FinancialInstruments):
    # properties
    pass

@dataclass
class Derivative(FinancialInstruments):
    # properties
    pass

@dataclass
class MutualFund(FinancialInstruments):
    # properties
    pass

@dataclass
class ETF(FinancialInstruments):
    # properties
    pass

@dataclass
class CommodityAndRealAssets(FinancialInstruments):
    storage_cost: float
    pass

@dataclass
class Cryptocurrencies(FinancialInstruments):
    pass


@dataclass
class CentralBank(Government):
    pass

@dataclass
class SecuritiesAndExchangeCommission(Regulators):
    pass

@dataclass
class CorporateBond(DebtInstrument):
    pass

@dataclass
class GovernmentBond(DebtInstrument):
    pass

@dataclass
class MunicipalBond(DebtInstrument):
    pass

@dataclass
class MortgageBackedSecurity(DebtInstrument):
    pass

@dataclass
class AssetBackedSecurity(DebtInstrument):
    pass

# TODO: !
@dataclass
class CollateralizedDebtObligation(DebtInstrument):
    pass

@dataclass
class CommonStock(EquityInstruments):
    pass

@dataclass
class PreferredStock(EquityInstruments):
    pass

@dataclass
class Warrant(EquityInstruments):
    pass

@dataclass
class Option(Derivative):
    pass

@dataclass
class Future(Derivative):
    pass

@dataclass
class Forward(Derivative):
    pass

@dataclass
class Swap(Derivative):
    pass

@dataclass
class Commodity(Derivative):
    pass

@dataclass
class IndexFund(MutualFund):
    pass

@dataclass
class BondFund(MutualFund):
    pass

@dataclass
class HedgeFund(MutualFund):
    pass

@dataclass
class RealEstateInvestmentTrust(MutualFund):
    pass

@dataclass
class ExchangeTradedFund(ETF):
    pass

@dataclass
class CommodityETF(ETF):
    pass

@dataclass
class CurrencyETF(ETF):
    pass

@dataclass
class RealEstateETF(ETF):
    pass

@dataclass
class CryptocurrencyETF(ETF):
    pass

#### Relations ####
@dataclass
class Issuance:
    financial_instrument: FinancialInstruments
    issuer: FinancialInstitutions

@dataclass
class RegulatoryOversight:
    regulator: Regulators
    entity: Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]

@dataclass
class MarketParticipation:
    financial_instrument: FinancialInstruments
    market: FinancialMarket

@dataclass
class Compliance:
    financial_institution: FinancialInstitutions
    regulator: Regulators
    compliant: bool

@dataclass
class JurisdictionalScope:
    jurisdiction: JudicialEntity
    applicable_entities: List[Union[FinancialInstitutions, FinancialMarket]]

@dataclass
class PolicyImpact:
    policy: GovernmentPolicy
    affected_entities: List[Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]]
    policy_maker: Government

@dataclass
class FiscalPolicyImpact(PolicyImpact):
    policy: FiscalPolicy
    affected_entities: List[Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]]
    policy_maker: Government

@dataclass
class MonetaryPolicyImpact(PolicyImpact):
    policy: MonetaryPolicy
    affected_entities: List[Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]]
    policy_maker: CentralBank

@dataclass
class FinancialRegulationImpact(PolicyImpact):
    policy: FinancialRegulation
    affected_entities: List[Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]]
    policy_maker: Regulators

# @dataclass
# class FinancialStability():
#     pass

# @dataclass
# class FinancialSystem():
#     pass

# @dataclass
# class FinancialCrisis():
#     pass


bond = DebtInstrument(annual_return=0.05, interest_rate=0.05, issuer="Bank")
