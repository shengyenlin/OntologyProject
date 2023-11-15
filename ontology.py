from dataclasses import dataclass
from typing import List
from typing import Union
import datetime


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
class FinancialInstruments:
    # properties
    name: str
    annual_return: float
    risk: float
    issued_institution: JudicialEntity # TODO: modify to a subclass of JudicialEntity
    market: JudicialEntity # TODO: modify to a subclass of JudicialEntity, market where this financial instrument is traded
    commodity_value_as_of_execution_date: float
    nominal_value: float
    principal_executive_office_address: str
    redemption_terms: str

@dataclass
class DebtInstrument(FinancialInstruments):
    # properties
    interest_rate: float
    issuer: str
    market: str

@dataclass
class Bond(DebtInstrument):
    award_date: datetime.date
    call_price: float
    call_rate_basis: str
    convertible_date: datetime.date
    extraordinary_redemption_provision: str
    funding_source: str

@dataclass
class Loan(DebtInstrument):
    # Loan specific properties
    maturity_date: datetime.date  # 0 or more explicit dates
    negative_amortization: bool  # Boolean value
    principal_amount: float  # Some loan principal
    nominal_value: float  # 0 or more monetary amounts
    disbursement_date: datetime.date  # Domain loan

@dataclass
class GovernmentDebtInstrument(DebtInstrument):
    # Inherited properties from Financial Instrument
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    maturity_date: datetime.date

@dataclass
class Equity(FinancialInstruments):
    # Inherited properties from FinancialInstruments
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    share_type: str  # Type of the share (e.g., common, preferred)
    dividend_yield: float  # Dividend yield, if applicable
    voting_rights: bool  # Indicates whether the share has voting rights

@dataclass
class CommonStock(Equity):
    # Properties specific to CommonStock
    dividend: float  # Minimum 0 ordinary dividend
    floating_shares: int  # Minimum 0 non-negative integer
    share_class: str  # Minimum 0 string to represent share class
    share_payment_status: 'SharePaymentStatus'  # Some share payment status
    shares_authorized: int  # Some non-negative integer

@dataclass
class PreferredStock(Equity):
    # Properties specific to PreferredStock
    dividend: Union['OrdinaryDividend', 'PreferredDividend']  # Some ordinary or preferred dividend
    maturity_date: datetime.date  # Minimum 0 explicit date
    is_senior_to_common_share: bool  # Indicates if it is senior to common share
    floating_shares: int  # Minimum 0 non-negative integer
    share_class: str  # Minimum 0 string to represent share class
    shares_authorized: int  # Some non-negative integer


@dataclass
class RestrictedStock(Equity):
    # Specific properties for RestrictedShare
    enhanced_voting: bool  # Indicates if the share has enhanced voting rights
    non_voting: bool  # Indicates if the share is non-voting
    fully_paid: bool  # Indicates if the share is fully paid
    nil_paid: bool  # Indicates if the share is nil paid
    partly_paid: bool  # Indicates if the share is partly paid

    # Inherited properties from Equity
    floating_shares: int  # Minimum 0 non-negative integer
    share_class: str  # Minimum 0 string to represent share class
    shares_authorized: int  # Some non-negative integer

@dataclass
class Derivative(FinancialInstruments):
    nominal_value: float  # 0 or more monetary amounts
    effective_date: datetime.date  # 0 or more dates
    execution_date: datetime.date  # 0 or more dates

@dataclass
class Forward(Derivative):
    nominal_value: float  # 0 or more monetary amounts
    effective_date: datetime.date  # 0 or more dates
    execution_date: datetime.date  # 0 or more dates

@dataclass
class Option(Derivative):
    # Specific properties for Option
    lot_size: float  # Some decimal value for lot size
    nominal_value: float  # 0 or more monetary amounts
    effective_date: datetime.date  # 0 or more dates
    execution_date: datetime.date  # 0 or more dates

@dataclass
class Future(Derivative):
    # Specific properties for Future
    # Properties that are typically relevant to futures contracts
    settlement_date: datetime.date  # The date by which the contract is to be settled
    contract_size: float  # The size or quantity of the asset in the contract
    tick_size: float  # The minimum price increment of the traded instrument
    nominal_value: float  # 0 or more monetary amounts
    effective_date: datetime.date  # 0 or more dates
    execution_date: datetime.date  # 0 or more dates

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
    entity: Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]
    regulation: FinancialRegulation
    is_compliant: bool
    compliance_details: str  # Added to give context to the compliance status.

@dataclass
class JurisdictionalScope:
    jurisdiction: JudicialEntity
    applicable_entities: List[Union[FinancialInstitutions, FinancialMarket]]

@dataclass
class PolicyImpact:
    policy: GovernmentPolicy
    affected_entities: List[Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]]
    effect_analysis: str  # Replaced policy_maker with effect_analysis.

@dataclass
class FiscalPolicyImpact(PolicyImpact):
    pass  # Inherits directly from PolicyImpact

@dataclass
class MonetaryPolicyImpact(PolicyImpact):
    central_bank: CentralBank  # Changed policy_maker to central_bank.

@dataclass
class FinancialRegulationImpact(PolicyImpact):
    regulator: Regulators  # Changed policy_maker to regulator.

@dataclass
class IsIssuedBy:
    instrument: FinancialInstruments
    institution: FinancialInstitutions
    issue_date: date
    issue_price: float

@dataclass
class IsRegulatedBy:
    instrument: FinancialInstruments
    regulator: Regulators
    regulation_effective_date: date
    regulation_id: str

@dataclass
class IsTradedIn:
    instrument: FinancialInstruments
    market: FinancialMarket
    trading_start_date: date
    trading_volume: float

@dataclass
class IsAffectedBy:
    instrument: FinancialInstruments
    policy: GovernmentPolicy
    policy_effect_date: date
    policy_impact_description: str

@dataclass
class OperatesIn:
    financial_institution: FinancialInstitutions
    financial_market: FinancialMarket

@dataclass
class RegulatesMarket:
    regulator: Regulators
    market: FinancialMarket

@dataclass
class SetsPolicyForMarket:
    policy: GovernmentPolicy
    market: FinancialMarket

@dataclass
class SupervisesInstitution:
    regulator: Regulators
    financial_institution: FinancialInstitutions

@dataclass
class IssuesSecurities:
    government: Government
    security: Union[Bond, DebtInstrument]

@dataclass
class ProvidesRating:
    rating_agency: CreditRatingAgency
    financial_instrument: FinancialInstruments
    rating: str

@dataclass
class OffersInsurance:
    insurance_company: InsuranceCompanies
    insured_entity: Union[FinancialInstruments, FinancialInstitutions, JudicialEntity]
    policy_details: str

@dataclass
class EnforcesRegulation:
    regulator: Regulators
    regulation: FinancialRegulation

@dataclass
class InfluencesMarketThroughPolicy:
    policy: GovernmentPolicy
    market: FinancialMarket
    impact_description: str

@dataclass
class EnactsMonetaryPolicy:
    central_bank: CentralBank  # Adjusted from Government to CentralBank for specificity.
    monetary_policy: MonetaryPolicy

@dataclass
class ImplementsFiscalPolicy:
    government: Government
    fiscal_policy: FiscalPolicy

@dataclass
class RegulatesFinancialInstrument:
    regulator: Regulators
    financial_instrument: FinancialInstruments

@dataclass
class SupervisoryAuthorityOverMarket:
    regulator: Regulators
    market: FinancialMarket

@dataclass
class ComplianceWithRegulation:
    entity: Union[FinancialInstruments, FinancialInstitutions, FinancialMarket]
    regulation: FinancialRegulation
    is_compliant: bool

@dataclass
class AdvisoryRole:
    advisor: Union[Regulators, Government]
    advisee: Union[FinancialInstitutions, FinancialMarket]
    advisory_purpose: str

@dataclass
class HoldBy:
    holder: Union[FinancialInstitutions, JudicialEntity, Regulators, Government]
    financial_instrument: FinancialInstruments
    holding_amount: float
    holding_date: date

@dataclass
class UnderlyingAsset:
    derivative: Derivative
    underlying_instrument: FinancialInstruments
    relation_description: str

@dataclass
class RegulationCompliance:
    entity: Union[FinancialInstruments, FinancialInstitutions]
    regulation: FinancialRegulation
    is_compliant: bool
    compliance_details: str

@dataclass
class RegulatoryReview:
    regulator: Regulators
    entity: Union[FinancialInstruments, FinancialInstitutions]
    review_outcome: str
    review_date: date

@dataclass
class PolicyInstrumentEffect:
    policy: GovernmentPolicy
    financial_instrument: FinancialInstruments
    effect_analysis: str

@dataclass
class RegulatoryImpactAssessment:
    regulator: Regulators
    market: FinancialMarket
    impact_assessment: str
    assessment_date: date

@dataclass
class PolicyMarketEffect:
    policy: GovernmentPolicy
    market: FinancialMarket
    effect_analysis: str



from datetime import date, datetime

# Instantiate Financial Markets
nyse = StockExchange(
    name="New York Stock Exchange",
    country="USA",
    currency="USD",
    timezone="EST",
    opening_time="09:30",
    closing_time="16:00"
)

# Instantiate Financial Institutions
goldman_sachs = SecuritiesFirms(
    Jurisdiction="USA",
    RegulatoryAuthority="SEC",
    LegalSystem="Federal"
)

# Instantiate Regulators
sec = Regulators(
    Jurisdiction="USA",
    RegulatoryAuthority="Securities and Exchange Commission",
    LegalSystem="Federal"
)

# Instantiate Government Policies
dodd_frank = FinancialRegulation(
    Jurisdiction="USA",
    RegulatoryAuthority="SEC",
    LegalSystem="Federal"
)

# Instantiate Financial Instruments
apple_stock = CommonStock(
    name="Apple Inc. Common Stock",
    annual_return=0.07,
    risk=0.3,
    issued_institution=goldman_sachs,  # Assuming Goldman Sachs was the underwriter
    market=nyse,
    commodity_value_as_of_execution_date=135.00,
    nominal_value=135.00,
    principal_executive_office_address="One Apple Park Way, Cupertino, California, U.S.",
    redemption_terms="N/A",
    dividend=0.85,
    floating_shares=16700000000,
    share_class="Common Stock",
    share_payment_status="Paid",
    shares_authorized=16700000000,
    share_type="Common",
    dividend_yield=0.0063,
    voting_rights=True
)

# Instantiate Regulatory Oversight
sec_oversight_apple = RegulatoryOversight(
    regulator=sec,
    entity=apple_stock
)

# Instantiate Market Participation
apple_participation_nyse = MarketParticipation(
    financial_instrument=apple_stock,
    market=nyse
)

# Instantiate Compliance
apple_compliance = Compliance(
    financial_institution=goldman_sachs,
    regulator=sec,
    compliant=True
)

# Instantiate Regulatory Impact Assessment
regulatory_impact_dodd_frank_nyse = RegulatoryImpactAssessment(
    regulator=sec,
    market=nyse,
    impact_assessment="Increased reporting requirements for listed companies.",
    assessment_date=date(2023, 1, 1)
)

# Instantiate Issuance
apple_issuance = Issuance(
    financial_instrument=apple_stock,
    issuer=goldman_sachs
)

# Instantiate Compliance with Regulation
apple_dodd_frank_compliance = ComplianceWithRegulation(
    entity=apple_stock,
    regulation=dodd_frank,
    is_compliant=True
)

# Instantiate Regulatory Review
sec_review_of_goldman = RegulatoryReview(
    regulator=sec,
    entity=goldman_sachs,
    review_outcome="Compliant with all regulations as of last review.",
    review_date=date(2023, 1, 1)
)

# Instantiate Policy Market Effect
dodd_frank_effect_on_nyse = PolicyMarketEffect(
    policy=dodd_frank,
    market=nyse,
    effect_analysis="The Dodd-Frank Act has led to increased stability in the NYSE through stringent compliance measures."
)

# Instantiate a Credit Rating Agency
moodys = CreditRatingAgency(
    Jurisdiction="USA",
    RegulatoryAuthority="SEC",
    LegalSystem="Federal"
)

# Instantiate a Government Body
us_treasury = Government(
    Jurisdiction="USA",
    RegulatoryAuthority="Department of the Treasury",
    LegalSystem="Federal"
)

# Instantiate a Financial Instrument (U.S. Treasury Bond)
us_treasury_bond = GovernmentDebtInstrument(
    name="U.S. Treasury Bond",
    annual_return=0.02,  # Approximate return rate for illustrative purposes
    risk=0.1,  # Treasury bonds are generally considered low risk
    issued_institution=us_treasury,
    market=nyse,
    commodity_value_as_of_execution_date=100.00,
    nominal_value=100.00,
    principal_executive_office_address="1500 Pennsylvania Avenue, NW, Washington, D.C.",
    redemption_terms="30 Year Bond",
    effective_date_time_stamp=datetime(2022, 1, 1),
    execution_date=date(2022, 1, 1),
    maturity_date=date(2052, 1, 1)
)

# Instantiate Issuance of the U.S. Treasury Bond
us_treasury_bond_issuance = Issuance(
    financial_instrument=us_treasury_bond,
    issuer=us_treasury
)

# Instantiate Rating Provided by Moody's
moodys_rating_for_treasury_bond = ProvidesRating(
    rating_agency=moodys,
    financial_instrument=us_treasury_bond,
    rating="Aaa"
)

# Instantiate a Financial Market (U.S. Bond Market)
us_bond_market = BondMarket(
    name="U.S. Bond Market",
    country="USA",
    currency="USD",
    timezone="EST",
    opening_time="08:00",
    closing_time="17:00"
)

# Instantiate Market Participation of U.S. Treasury Bond in the U.S. Bond Market
treasury_bond_participation_us_bond_market = MarketParticipation(
    financial_instrument=us_treasury_bond,
    market=us_bond_market
)

# Instantiate Regulatory Oversight by the SEC on Moody's
sec_oversight_moodys = RegulatoryOversight(
    regulator=sec,
    entity=moodys
)

# Instantiate a Fiscal Policy (U.S. Federal Budget)
us_federal_budget = FiscalPolicy(
    Jurisdiction="USA",
    RegulatoryAuthority="Congress",
    LegalSystem="Federal"
)

# Instantiate Fiscal Policy Impact on U.S. Treasury Bond
federal_budget_impact_on_treasury_bond = FiscalPolicyImpact(
    policy=us_federal_budget,
    affected_entities=[us_treasury_bond],
    effect_analysis="The federal budget deficit has led to increased issuance of Treasury bonds."
)

# Instantiate Monetary Policy (Federal Reserve Interest Rate Decision)
fed_interest_rate_decision = MonetaryPolicy(
    Jurisdiction="USA",
    RegulatoryAuthority="Federal Reserve",
    LegalSystem="Federal"
)

# Instantiate Monetary Policy Impact on the U.S. Bond Market
fed_policy_impact_on_bond_market = MonetaryPolicyImpact(
    policy=fed_interest_rate_decision,
    affected_entities=[us_bond_market],
    effect_analysis="The Federal Reserve's decision to change the interest rate affected the bond yields."
)

# Instantiate a Supervisory Authority Role of the SEC over the NYSE
sec_supervisory_authority_nyse = SupervisoryAuthorityOverMarket(
    regulator=sec,
    market=nyse
)

# Instantiate Compliance with Regulation (Dodd-Frank Act Compliance Check for Goldman Sachs)
goldman_sachs_dodd_frank_compliance = ComplianceWithRegulation(
    entity=goldman_sachs,
    regulation=dodd_frank,
    is_compliant=True
)

# Instantiate an Advisory Role (SEC Advisory to NYSE)
sec_advisory_to_nyse = AdvisoryRole(
    advisor=sec,
    advisee=nyse,
    advisory_purpose="Guidance on enhancing market surveillance systems."
)

# Instantiate a Corporate Bond from a known company
tesla_corporate_bond = Bond(
    name="Tesla Inc. 5% 2025 Corporate Bond",
    annual_return=0.05,
    risk=0.2,
    issued_institution=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",  # Financial Industry Regulatory Authority
        LegalSystem="Federal"
    ),
    market=nyse,
    commodity_value_as_of_execution_date=105.00,
    nominal_value=100.00,
    principal_executive_office_address="3500 Deer Creek Road, Palo Alto, CA",
    redemption_terms="Callable",
    award_date=date(2020, 9, 1),
    call_price=102.00,
    call_rate_basis="5% Annual",
    convertible_date=date(2023, 9, 1),
    extraordinary_redemption_provision="Yes",
    funding_source="Corporate Earnings"
)

# Instantiate a Municipal Bond
san_francisco_municipal_bond = Bond(
    name="San Francisco Water Revenue 4% 2030 Municipal Bond",
    annual_return=0.04,
    risk=0.1,
    issued_institution=Government(
        Jurisdiction="USA",
        RegulatoryAuthority="Municipal Securities Rulemaking Board",
        LegalSystem="State"
    ),
    market=us_bond_market,
    commodity_value_as_of_execution_date=102.00,
    nominal_value=100.00,
    principal_executive_office_address="1 Dr Carlton B Goodlett Pl, San Francisco, CA 94102",
    redemption_terms="Non-Callable",
    award_date=date(2022, 4, 15),
    call_price=100.00,
    call_rate_basis="4% Annual",
    convertible_date=date(2025, 4, 15),
    extraordinary_redemption_provision="No",
    funding_source="Municipal Water Revenue"
)

# Instantiate an Exchange-Traded Fund (ETF)
sp500_etf = FinancialInstruments(
    name="SPDR S&P 500 ETF Trust",
    annual_return=0.1,  # Historical average return
    risk=0.15,
    issued_institution=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    market=nyse,
    commodity_value_as_of_execution_date=415.00,  # The example price for the ETF
    nominal_value=415.00,
    principal_executive_office_address="State Street Bank and Trust Company, One Lincoln Street, Boston, MA 02111",
    redemption_terms="Redeemable"
)

# Instantiate Stocks of well-known companies
amazon_stock = CommonStock(
    name="Amazon Inc. Common Stock",
    annual_return=0.15,  # Hypothetical return
    risk=0.25,
    issued_institution=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    market=nyse,
    commodity_value_as_of_execution_date=3300.00,
    nominal_value=3300.00,
    principal_executive_office_address="410 Terry Ave N, Seattle, WA 98109",
    redemption_terms="N/A",
    dividend=0.0,
    floating_shares=500000000,
    share_class="Common",
    share_payment_status="Paid",
    shares_authorized=500000000,
    share_type="Common",
    dividend_yield=0.0,
    voting_rights=True
)

google_stock = CommonStock(
    name="Alphabet Inc. (Google) Common Stock",
    annual_return=0.22,  # Hypothetical return
    risk=0.2,
    issued_institution=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    market=nyse,
    commodity_value_as_of_execution_date=2800.00,
    nominal_value=2800.00,
    principal_executive_office_address="1600 Amphitheatre Parkway, Mountain View, California, U.S.",
    redemption_terms="N/A",
    dividend=0.0,
    floating_shares=300000000,
    share_class="Common",
    share_payment_status="Paid",
    shares_authorized=300000000,
    share_type="Common",
    dividend_yield=0.0,
    voting_rights=True
)

# Instantiate the Issuance of Tesla Corporate Bond
tesla_bond_issuance = Issuance(
    financial_instrument=tesla_corporate_bond,
    issuer=goldman_sachs  # Assuming Goldman Sachs as the underwriter
)

# Instantiate the Regulatory Oversight by SEC on Tesla Corporate Bond
sec_oversight_tesla_bond = RegulatoryOversight(
    regulator=sec,
    entity=tesla_corporate_bond
)

# Instantiate the Market Participation of Tesla Corporate Bond in the NYSE
tesla_bond_nyse_participation = MarketParticipation(
    financial_instrument=tesla_corporate_bond,
    market=nyse
)

# Instantiate the Compliance of Tesla Corporate Bond with SEC Regulations
tesla_bond_sec_compliance = Compliance(
    financial_institution=goldman_sachs,
    regulator=sec,
    compliant=True
)

# Instantiate the Jurisdictional Scope of SEC
sec_jurisdictional_scope = JurisdictionalScope(
    jurisdiction=sec,
    applicable_entities=[nyse, us_bond_market]
)

# Instantiate the Policy Impact of Dodd-Frank Act on Financial Instruments
dodd_frank_policy_impact = PolicyImpact(
    policy=dodd_frank,
    affected_entities=[tesla_corporate_bond, amazon_stock, google_stock],
    effect_analysis="The Dodd-Frank Act has implemented stricter capital requirements and risk management protocols."
)

# Instantiate the Fiscal Policy Impact of U.S. Federal Budget on Government Bonds
us_federal_budget_impact = FiscalPolicyImpact(
    policy=us_federal_budget,
    affected_entities=[us_treasury_bond],
    policy_maker=us_treasury  # The Treasury is typically involved in fiscal policy through budgeting.
)

# Instantiate the Monetary Policy Impact of Federal Reserve on the NYSE
fed_policy_nyse_impact = MonetaryPolicyImpact(
    policy=fed_interest_rate_decision,
    affected_entities=[nyse],
    central_bank=us_treasury  # The Federal Reserve is the central bank in this scenario.
)

# Instantiate the Financial Regulation Impact of SEC on Tesla Corporate Bond
sec_regulation_tesla_impact = FinancialRegulationImpact(
    policy=dodd_frank,
    affected_entities=[tesla_corporate_bond],
    regulator=sec
)

# Instantiate the IsIssuedBy relationship for Amazon Stock
amazon_stock_issuance = IsIssuedBy(
    instrument=amazon_stock,
    institution=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    issue_date=date(1997, 5, 15),  # Amazon's IPO date
    issue_price=18.00  # Amazon's IPO price
)

# Instantiate the IsRegulatedBy relationship for Amazon Stock
amazon_stock_regulation = IsRegulatedBy(
    instrument=amazon_stock,
    regulator=sec,
    regulation_effective_date=date(1997, 5, 15),
    regulation_id="AMZN_SEC_REG_1997"
)

# Instantiate the IsTradedIn relationship for Amazon Stock
amazon_stock_nyse_trading = IsTradedIn(
    instrument=amazon_stock,
    market=nyse,
    trading_start_date=date(1997, 5, 15),
    trading_volume=3_000_000  # Hypothetical trading volume on IPO date
)

# Instantiate the IsAffectedBy relationship for Google Stock
google_stock_policy_effect = IsAffectedBy(
    instrument=google_stock,
    policy=dodd_frank,
    policy_effect_date=date(2010, 7, 21),  # Dodd-Frank Act enactment date
    policy_impact_description="The enactment of the Dodd-Frank Act has increased compliance costs for Google."
)

# Instantiate SupervisesInstitution relationship for SEC over Goldman Sachs
sec_supervision_goldman = SupervisesInstitution(
    regulator=sec,
    financial_institution=goldman_sachs
)

# Instantiate IssuesSecurities relationship for U.S. Treasury issuing a bond
us_treasury_issues_bond = IssuesSecurities(
    government=us_treasury,
    security=us_treasury_bond
)

# Instantiate ProvidesRating relationship for Moody's rating on Tesla Bond
moodys_rating_tesla_bond = ProvidesRating(
    rating_agency=moodys,
    financial_instrument=tesla_corporate_bond,
    rating="Baa1"  # Hypothetical Moody's rating
)

# Instantiate OffersInsurance relationship for an insurance company insuring Tesla Corporate Bond
insurance_on_tesla_bond = OffersInsurance(
    insurance_company=InsuranceCompanies(
        Jurisdiction="USA",
        RegulatoryAuthority="Federal Insurance Office",
        LegalSystem="Federal"
    ),
    insured_entity=tesla_corporate_bond,
    policy_details="Insurance against default on corporate bond"
)

# Instantiate EnforcesRegulation relationship for SEC enforcing the Dodd-Frank Act
sec_enforces_dodd_frank = EnforcesRegulation(
    regulator=sec,
    regulation=dodd_frank
)

# Instantiate InfluencesMarketThroughPolicy relationship for the Dodd-Frank Act's influence on the NYSE
dodd_frank_influences_nyse = InfluencesMarketThroughPolicy(
    policy=dodd_frank,
    market=nyse,
    impact_description="The Dodd-Frank Act has reinforced market integrity and investor confidence in the NYSE."
)

# Instantiate EnactsMonetaryPolicy relationship for Federal Reserve's monetary policy
fed_enacts_policy = EnactsMonetaryPolicy(
    central_bank=CentralBank(
        Jurisdiction="USA",
        RegulatoryAuthority="Federal Reserve",
        LegalSystem="Federal"
    ),
    monetary_policy=fed_interest_rate_decision
)

# Instantiate ImplementsFiscalPolicy relationship for U.S. Government's fiscal policy
us_government_implements_fiscal_policy = ImplementsFiscalPolicy(
    government=us_treasury,
    fiscal_policy=us_federal_budget
)

# Instantiate RegulatesFinancialInstrument relationship for SEC regulation on Google Stock
sec_regulates_google_stock = RegulatesFinancialInstrument(
    regulator=sec,
    financial_instrument=google_stock
)

# Instantiate SupervisoryAuthorityOverMarket relationship for SEC supervision over the Bond Market
sec_supervisory_authority_bond_market = SupervisoryAuthorityOverMarket(
    regulator=sec,
    market=us_bond_market
)

# Instantiate ComplianceWithRegulation relationship for Amazon's compliance with SEC regulations
amazon_compliance_with_sec = ComplianceWithRegulation(
    entity=amazon_stock,
    regulation=dodd_frank,
    is_compliant=True
)

# Instantiate AdvisoryRole relationship for SEC's advisory role to the Cryptocurrency Market
sec_advisory_to_crypto_market = AdvisoryRole(
    advisor=sec,
    advisee=CryptocurrencyMarket(
        name="U.S. Cryptocurrency Market",
        country="USA",
        currency="USD",
        timezone="EST",
        opening_time="24/7",
        closing_time="24/7"
    ),
    advisory_purpose="Guidance on regulatory compliance for cryptocurrency exchanges."
)

# Instantiate HoldBy relationship for a hypothetical investment firm holding Amazon Stock
investment_firm_holds_amazon = HoldBy(
    holder=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    financial_instrument=amazon_stock,
    holding_amount=5000,
    holding_date=date(2021, 1, 1)
)

# Instantiate UnderlyingAsset relationship for a derivative instrument based on Google Stock
derivative_on_google = UnderlyingAsset(
    derivative=Option(
        name="Call Option on Google Stock",
        annual_return=0.2,  # Hypothetical return for the option
        risk=0.5,  # Options carry higher risk
        issued_institution=SecuritiesFirms(
            Jurisdiction="USA",
            RegulatoryAuthority="FINRA",
            LegalSystem="Federal"
        ),
        market=nyse,
        commodity_value_as_of_execution_date=3000.00,  # Hypothetical market value of the option
        nominal_value=3000.00,
        effective_date=date(2023, 1, 1),
        execution_date=date(2023, 1, 1)
    ),
    underlying_instrument=google_stock,
    relation_description="This call option gives the right to buy Google Stock at a set price."
)

# Instantiate RegulatoryImpactAssessment relationship for the impact of SEC regulations on Tesla Bonds
sec_impact_assessment_tesla = RegulatoryImpactAssessment(
    regulator=sec,
    market=nyse,
    impact_assessment="Stringent SEC regulations have led to increased disclosure requirements for Tesla bonds.",
    assessment_date=date.today()
)

# Instantiate PolicyMarketEffect relationship for the impact of monetary policy on the Foreign Exchange Market
fed_policy_fx_market_effect = PolicyMarketEffect(
    policy=fed_interest_rate_decision,
    market=ForeignExchangeMarket(
        name="Forex",
        country="International",
        currency="Multiple",
        timezone="EST",
        opening_time="24/7",
        closing_time="24/7"
    ),
    effect_analysis="Federal Reserve's interest rate decisions have a significant impact on currency valuations and Forex market volatility."
)

# Instantiate a relationship for the impact of fiscal policy on the Money Market
us_fiscal_policy_money_market_impact = FiscalPolicyImpact(
    policy=us_federal_budget,
    affected_entities=[MoneyMarket(
        name="U.S. Money Market",
        country="USA",
        currency="USD",
        timezone="EST",
        opening_time="09:00",
        closing_time="17:00"
    )],
    policy_maker=us_treasury
)

# Instantiate a relationship for the issuance of a new ETF
sp500_etf_issuance = Issuance(
    financial_instrument=sp500_etf,
    issuer=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    )
)

# Instantiate a relationship for the compliance of SPDR S&P 500 ETF with SEC regulations
sp500_etf_sec_compliance = Compliance(
    financial_institution=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    regulator=sec,
    compliant=True
)

# Instantiate a relationship for the regulatory oversight of Moody's over San Francisco Municipal Bond
moodys_oversight_sf_muni_bond = RegulatoryOversight(
    regulator=moodys,
    entity=san_francisco_municipal_bond
)

# Instantiate a relationship for the trading of the San Francisco Municipal Bond in the U.S. Bond Market
sf_muni_bond_trading = MarketParticipation(
    financial_instrument=san_francisco_municipal_bond,
    market=us_bond_market
)

# Instantiate a relationship for the impact of regulatory changes on Amazon Stock
sec_regulatory_changes_amazon_impact = RegulatoryImpactAssessment(
    regulator=sec,
    market=nyse,
    impact_assessment="Recent SEC regulatory changes have necessitated additional compliance measures by Amazon.",
    assessment_date=date.today()
)

# Instantiate a relationship for the advisory role of the SEC towards Goldman Sachs regarding new financial instruments
sec_advisory_goldman_new_instruments = AdvisoryRole(
    advisor=sec,
    advisee=goldman_sachs,
    advisory_purpose="Advisory on the introduction of new financial instruments and associated regulatory compliance."
)

# Instantiate a relationship for the holding of Google Stock by an investment firm
investment_firm_holds_google = HoldBy(
    holder=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    financial_instrument=google_stock,
    holding_amount=10000,
    holding_date=date(2021, 6, 1)
)


# Instantiate a relationship for Moody's providing a credit rating to Amazon's corporate bonds
moodys_rating_amazon_bonds = ProvidesRating(
    rating_agency=moodys,
    financial_instrument=DebtInstrument(
        name="Amazon 10-Year Corporate Bond",
        annual_return=0.04,  # Hypothetical return
        risk=0.2,
        issued_institution=goldman_sachs,
        market=us_bond_market,
        commodity_value_as_of_execution_date=100.00,
        nominal_value=100.00,
        principal_executive_office_address="410 Terry Ave N, Seattle, WA 98109",
        redemption_terms="Non-Callable",
        interest_rate=0.04
    ),
    rating="Aa2"  # Hypothetical Moody's rating
)

# Instantiate a relationship for the SEC enforcing regulations on the Cryptocurrency Market
sec_enforces_crypto_regulations = EnforcesRegulation(
    regulator=sec,
    regulation=FinancialRegulation(
        Jurisdiction="USA",
        RegulatoryAuthority="SEC",
        LegalSystem="Federal"
    )  # Assume this regulation is specific to cryptocurrencies
)

# Instantiate a relationship for the impact of U.S. Federal Budget on San Francisco Municipal Bonds
us_budget_impact_sf_muni_bonds = FiscalPolicyImpact(
    policy=us_federal_budget,
    affected_entities=[san_francisco_municipal_bond],
    policy_maker=us_treasury
)

# Instantiate a relationship for Goldman Sachs' compliance with SEC regulations
goldman_sachs_sec_compliance = ComplianceWithRegulation(
    entity=goldman_sachs,
    regulation=dodd_frank,
    is_compliant=True
)

# Instantiate a relationship for the trading of Tesla Corporate Bonds in the U.S. Bond Market
tesla_bond_us_bond_market_trading = IsTradedIn(
    instrument=tesla_corporate_bond,
    market=us_bond_market,
    trading_start_date=date(2020, 9, 2),  # Assume trading starts the day after issuance
    trading_volume=500000  # Hypothetical trading volume
)

# Instantiate a relationship for the effect of U.S. monetary policy on Tesla Corporate Bonds
fed_policy_effect_tesla_bonds = MonetaryPolicyImpact(
    policy=fed_interest_rate_decision,
    affected_entities=[tesla_corporate_bond],
    central_bank=CentralBank(
        Jurisdiction="USA",
        RegulatoryAuthority="Federal Reserve",
        LegalSystem="Federal"
    )  # Assuming this is an instance of the Central Bank class
)

# Instantiate a relationship for the Federal Reserve setting monetary policy for the U.S. Money Market
fed_sets_policy_for_money_market = SetsPolicyForMarket(
    policy=fed_interest_rate_decision,
    market=MoneyMarket(
        name="U.S. Money Market Funds",
        country="USA",
        currency="USD",
        timezone="EST",
        opening_time="08:00",
        closing_time="18:00"
    )
)

# Instantiate a relationship for the SEC's supervision of the issuance of new government bonds
sec_supervises_new_gov_bond_issuance = SupervisoryAuthorityOverMarket(
    regulator=sec,
    market=us_bond_market
)

# Instantiate a relationship for the insurance of assets held by Goldman Sachs
insurance_on_goldman_assets = OffersInsurance(
    insurance_company=InsuranceCompanies(
        Jurisdiction="USA",
        RegulatoryAuthority="State Insurance Regulators",
        LegalSystem="State"
    ),
    insured_entity=goldman_sachs,
    policy_details="Asset insurance covering corporate bonds and other securities"
)

# Instantiate a relationship for an investment firm holding SPDR S&P 500 ETF Trust shares
investment_firm_holds_sp500_etf = HoldBy(
    holder=SecuritiesFirms(
        Jurisdiction="USA",
        RegulatoryAuthority="FINRA",
        LegalSystem="Federal"
    ),
    financial_instrument=sp500_etf,
    holding_amount=20000,
    holding_date=date(2021, 5, 1)
)

# Instantiate a relationship for an underlying asset of a derivative product tied to the S&P 500 index
sp500_etf_as_underlying_for_derivative = UnderlyingAsset(
    derivative=Derivative(
        name="S&P 500 Index Option",
        annual_return=0.15,  # Hypothetical return
        risk=0.5,
        issued_institution=SecuritiesFirms(
            Jurisdiction="USA",
            RegulatoryAuthority="FINRA",
            LegalSystem="Federal"
        ),
        market=nyse,
        commodity_value_as_of_execution_date=420.00,  # Hypothetical market value of the option
        nominal_value=420.00,
        effective_date=date(2023, 6, 
