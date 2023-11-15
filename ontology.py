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

    # Internal object properties
    commodity_value_as_of_execution_date: float
    nominal_value: float
    principal_executive_office_address: str
    redemption_terms: str
    shareholder: 'ShareholderSubclass'
    underlier: 'UnderlierSubclass'
    value_expressed_in: str
    holds_shares_in: 'CompanySubclass'
    denominated_in: str
    legally_recorded_in: str

    # External object properties
    acts_on: 'EntitySubclass'
    applies_to: 'EntitySubclass'
    comprises: list['FinancialInstrumentSubclass']
    borrower: 'EntitySubclass'
    contractual_element: str
    currency: str
    governing_jurisdiction: str
    lender: 'EntitySubclass'
    monetary_amount: float
    quantity_value: float
    registered_address: str
    identifies: str
    involves: 'EntitySubclass'
    is_a_party_to: 'ContractSubclass'
    is_affected_by: 'EventSubclass'
    is_identified_by: str
    is_included_in: 'CollectionSubclass'
    is_issued_by: 'IssuerSubclass'
    is_played_by: 'EntitySubclass'

@dataclass
class DebtInstrument(FinancialInstruments):
    # properties
    interest_rate: float
    issuer: str
    market: str

@dataclass
class Bond(DebtInstrument):
    # Internal object properties
    award_date: datetime.date
    call_price: float
    call_rate_basis: str
    convertible_date: datetime.date
    extraordinary_redemption_provision: str
    final_maturity_date: datetime.date
    first_call_price: float
    first_coupon_payment_date: datetime.date
    first_par_call_date: datetime.date
    first_par_call_price: float
    first_premium_call_date: datetime.date
    first_premium_call_price: float
    first_put_date: datetime.date
    first_put_price: float
    funding_source: str
    last_coupon_payment_date: datetime.date
    lockout_period: datetime.timedelta
    municipal_trustee: str
    original_issue_discount_amount: float
    partial_redemption_allocation_convention: str
    penultimate_coupon_payment_date: datetime.date
    premium_amount: float
    put_date: datetime.date
    put_frequency: str
    redemption_amount: float
    remarketing_agent: str
    reset_date_offset: datetime.timedelta
    linked_to_fallback: bool

    # External object properties
    comprises: list['FinancialInstrumentSubclass']
    defines_terms_for: str
    has_argument: str
    has_call_feature: bool
    has_contractual_element: str
    currency: str
    data_source: str
    date: datetime.date
    date_period: datetime.timedelta
    end_date: datetime.date
    explicit_date: datetime.date
    expression: str
    interest_payment_terms: str
    interest_rate: float
    monetary_amount: float
    objective: str
    price: float
    recurrence_interval: datetime.timedelta
    relative_price_at_issue: float
    relative_price_at_maturity: float
    repayment_terms: str
    schedule: 'ScheduleSubclass'
    start_date: datetime.date
    third_party: str
    involves: 'EntitySubclass'
    based_on: str
    denominated_in: str
    issued_by: 'IssuerSubclass'
    played_by: 'EntitySubclass'
    refers_to: str
    registers: str
    specifies_conversion_into: str

    # Internal data properties
    ceiling: float
    floor: float
    is_bank_qualified: bool
    is_legal_opinion_available: bool
    is_mandatory: bool
    is_pro_rated: bool
    super_sinker: bool

    # External data properties
    has_rate_value: float
    is_callable: bool

@dataclass
class Loan(DebtInstrument):
    # Loan specific properties
    corresponding_account: list['LoanSpecificCustomerAccount']  # 0 or more accounts
    guarantor: list['Guarantor']  # 0 or more guarantors
    maturity_date: datetime.date  # 0 or more explicit dates
    negative_amortization: bool  # Boolean value
    principal_amount: float  # Some loan principal

    # Inherited properties from DebtInstrument
    borrower: 'Borrower'
    call_feature: list['CallFeature']  # 0 or more call features
    interest_payment_terms: 'InterestPaymentTerms'
    lender: 'Lender'
    offering: list['DebtOffering']  # 0 or more offerings
    put_feature: list['PutFeature']  # 0 or more put features
    redemption_terms: 'RedemptionProvision'
    repayment_terms: 'PrincipalRepaymentTerms'

    # Inherited properties from Contract
    contract_party: list['ContractParty']  # 2 or more parties
    contractual_element: list['ContractualElement']  # Some contractual elements
    effective_date: datetime.date  # 0 or more dates

    # Inherited properties from CreditAgreement
    creditor: 'Creditor'
    debtor: 'Debtor'
    debt_terms: 'DebtTerms'
    loan_or_credit_account: list['LoanOrCreditAccount']  # 0 or more accounts

    # Inherited properties from FinancialInstrument
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: list['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: list['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: list['IndustrySectorClassifier']  # 0 or more classifiers

    # Additional properties based on the ontology
    disbursement_date: datetime.date  # Domain loan

    # ... Additional methods and logic as required ...

@dataclass
class GovernmentDebtInstrument(DebtInstrument):
    # Direct properties of Government Debt Instrument
    issuer: 'Polity'  # is issued by some polity (played by some polity)

    # Inherited properties from DebtInstrument
    borrower: 'Borrower'
    call_feature: List['CallFeature']  # 0 or more call features
    interest_payment_terms: 'InterestPaymentTerms'
    lender: 'Lender'
    offering: List['DebtOffering']  # 0 or more offerings

    # Inherited properties from Contract
    contract_party: List['ContractParty']  # 2 or more parties
    contractual_element: List['ContractualElement']

    # Inherited properties from Credit Agreement
    creditor: 'Creditor'
    debtor: 'Debtor'
    debt_terms: 'DebtTerms'
    corresponding_account: List['LoanOrCreditAccount']  # 0 or more accounts
    maturity_date: datetime.date  # 0 or more explicit dates

    # Inherited properties from Financial Instrument
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: List['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: List['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: List['IndustrySectorClassifier']  # 0 or more classifiers

    # Inherited properties from Written Contract
    counterparty: 'Counterparty'
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'

    # Additional properties specific to Government Debt Instrument can be added here

@dataclass
class Equity(FinancialInstruments):
    # Inherited properties from FinancialInstruments
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: List['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: List['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: List['IndustrySectorClassifier']  # 0 or more classifiers

    # Inherited properties from Contract
    contract_party: List['ContractParty']  # 2 or more parties
    contractual_element: List['ContractualElement']
    effective_date: datetime.date  # 0 or more dates

    # Inherited properties from Written Contract
    counterparty: 'Counterparty'
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'

    # Inherited properties from Security
    issued_in_form: List['SecurityForm']  # 0 or more forms
    legally_recorded_in: 'Jurisdiction'  # Exactly 1 jurisdiction
    registered: List['RegistrationAuthority']  # 0 or more authorities

    # Additional properties specific to Equity (Share)
    # Add any additional properties specific to shares here

    # Example of additional properties
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

    # Inherited properties from Equity
    # Assuming these properties are already defined in the Equity class
    # financial_instrument_short_name, nominal_value, securities_restriction,
    # financial_instrument_classifier, industry_sector_classifier,
    # contract_party, contractual_element, effective_date, etc.

    # Additional properties specific to common shares
    enhanced_voting_rights: bool  # Indicates enhanced voting rights
    restricted: bool  # Indicates if the shares are restricted
    fully_paid: bool  # Indicates if the shares are fully paid
    nil_paid: bool  # Indicates if the shares are nil paid
    partly_paid: bool  # Indicates if the shares are partly paid
    unrestricted: bool  # Indicates if the shares are unrestricted

    # Inherited properties from Contract
    counterparty: 'Counterparty'
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'

    # Additional methods and logic as required

@dataclass
class PreferredStock(Equity):
    # Properties specific to PreferredStock
    dividend: Union['OrdinaryDividend', 'PreferredDividend']  # Some ordinary or preferred dividend
    maturity_date: datetime.date  # Minimum 0 explicit date
    is_senior_to_common_share: bool  # Indicates if it is senior to common share

    # Inherited properties from Equity
    floating_shares: int  # Minimum 0 non-negative integer
    share_class: str  # Minimum 0 string to represent share class
    share_payment_status: 'SharePaymentStatus'  # Some share payment status
    shares_authorized: int  # Some non-negative integer

    # Additional properties specific to preferred shares
    convertible: bool  # Indicates if the share is a convertible preferred share
    cumulative: bool  # Indicates if the share is a cumulative preferred share
    exchangeable: bool  # Indicates if the share is an exchangeable preferred share
    extendable: bool  # Indicates if the share is an extendable preferred share
    non_cumulative: bool  # Indicates if the share is a non-cumulative preferred share

    # Inherited properties from Contract
    counterparty: 'Counterparty'
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'

    # Additional methods and logic as required

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
    share_payment_status: 'SharePaymentStatus'  # Some share payment status
    shares_authorized: int  # Some non-negative integer

    # Inherited properties from Financial Instrument
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: List['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: List['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: List['IndustrySectorClassifier']  # 0 or more classifiers

    # Inherited properties from Contract
    contract_party: List['ContractParty']  # 2 or more parties
    contractual_element: List['ContractualElement']
    effective_date: datetime.date  # 0 or more dates

    # Inherited properties from Written Contract
    counterparty: 'Counterparty'
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'

    # Additional methods and logic as required

@dataclass
class Derivative(FinancialInstruments):
    # Specific properties for Derivative
    derivative_terms: 'DerivativeTerms'  # Some derivative terms
    settlement_terms: 'SettlementTerms'  # Some settlement terms
    underlier: 'Underlier'  # Some underlier
    valuation_terms: 'ValuationTerms'  # Some valuation terms

    # Inherited properties from Financial Instruments
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: List['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: List['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: List['IndustrySectorClassifier']  # 0 or more classifiers

    # Inherited properties from Contract
    contract_party: List['ContractParty']  # 2 or more parties
    contractual_element: List['ContractualElement']  # Some contractual elements
    effective_date: datetime.date  # 0 or more dates

    # Inherited properties from Written Contract
    counterparty: 'Counterparty'  # Some counterparty
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'  # Some contract principal

    # Additional methods and logic as required

@dataclass
class Forward(Derivative):
    # Inherited properties from Derivative
    derivative_terms: 'DerivativeTerms'  # Some derivative terms
    settlement_terms: 'SettlementTerms'  # Some settlement terms
    underlier: 'Underlier'  # Some underlier
    valuation_terms: 'ValuationTerms'  # Some valuation terms

    # Additional properties specific to Forward
    # (if any specific properties are needed for the Forward class, add them here)

    # Inherited properties from Financial Instruments
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: List['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: List['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: List['IndustrySectorClassifier']  # 0 or more classifiers

    # Inherited properties from Contract
    contract_party: List['ContractParty']  # 2 or more parties
    contractual_element: List['ContractualElement']  # Some contractual elements
    effective_date: datetime.date  # 0 or more dates

    # Inherited properties from Written Contract
    counterparty: 'Counterparty'  # Some counterparty
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'  # Some contract principal

    # Additional methods and logic as required

@dataclass
class Option(Derivative):
    # Specific properties for Option
    lot_size: float  # Some decimal value for lot size

    # Inherited properties from Derivative
    derivative_terms: 'DerivativeTerms'  # Some derivative terms
    settlement_terms: 'SettlementTerms'  # Some settlement terms
    underlier: 'Underlier'  # Some underlier
    valuation_terms: 'ValuationTerms'  # Some valuation terms

    # Additional properties specific to Option
    # If there are any additional properties specific to options (e.g., strike price, expiration date), add them here

    # Inherited properties from Financial Instruments
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: List['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: List['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: List['IndustrySectorClassifier']  # 0 or more classifiers

    # Inherited properties from Contract
    contract_party: List['ContractParty']  # 2 or more parties
    contractual_element: List['ContractualElement']  # Some contractual elements
    effective_date: datetime.date  # 0 or more dates

    # Inherited properties from Written Contract
    counterparty: 'Counterparty'  # Some counterparty
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'  # Some contract principal

    # Additional methods and logic as required

@dataclass
class Future(Derivative):
    # Specific properties for Future
    # Properties that are typically relevant to futures contracts
    settlement_date: datetime.date  # The date by which the contract is to be settled
    contract_size: float  # The size or quantity of the asset in the contract
    tick_size: float  # The minimum price increment of the traded instrument

    # Inherited properties from Derivative
    derivative_terms: 'DerivativeTerms'  # Some derivative terms
    settlement_terms: 'SettlementTerms'  # Some settlement terms
    underlier: 'Underlier'  # Some underlier
    valuation_terms: 'ValuationTerms'  # Some valuation terms

    # Inherited properties from Financial Instruments
    financial_instrument_short_name: str  # 0 or more short names
    nominal_value: float  # 0 or more monetary amounts
    securities_restriction: List['SecuritiesRestriction']  # 0 or more restrictions
    financial_instrument_classifier: List['FinancialInstrumentClassifier']  # 0 or more classifiers
    industry_sector_classifier: List['IndustrySectorClassifier']  # 0 or more classifiers

    # Inherited properties from Contract
    contract_party: List['ContractParty']  # 2 or more parties
    contractual_element: List['ContractualElement']  # Some contractual elements
    effective_date: datetime.date  # 0 or more dates

    # Inherited properties from Written Contract
    counterparty: 'Counterparty'  # Some counterparty
    effective_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    execution_date: datetime.date  # 0 or more dates
    execution_date_time_stamp: datetime.datetime  # 0 or more date time stamps
    principal_party: 'ContractPrincipal'  # Some contract principal

    # Additional methods and logic as required


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
class SecutityCompany():
    pass


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

# TODO: fourth classes Turn to instances 
# @dataclass
# class Option(Derivative):
#     pass

# @dataclass
# class Future(Derivative):
#     pass

# @dataclass
# class Forward(Derivative):
#     pass

# @dataclass
# class Swap(Derivative):
#     pass

# @dataclass
# class Commodity(Derivative):
#     pass

# @dataclass
# class IndexFund(MutualFund):
#     pass

# @dataclass
# class BondFund(MutualFund):
#     pass

# @dataclass
# class HedgeFund(MutualFund):
#     pass

# @dataclass
# class RealEstateInvestmentTrust(MutualFund):
#     pass

# TODO: fourth classes Turn to instances 
# @dataclass
# class ExchangeTradedFund(ETF):
#     pass

# @dataclass
# class CommodityETF(ETF):
#     pass

# @dataclass
# class CurrencyETF(ETF):
#     pass

# @dataclass
# class RealEstateETF(ETF):
#     pass

# @dataclass
# class CryptocurrencyETF(ETF):
#     pass

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

# TODO: think about more relationships
# TODO: 

# @dataclass
# class FinancialStability():
#     pass

# @dataclass
# class FinancialSystem():
#     pass

# @dataclass
# class FinancialCrisis():
#     pass


convertible_bond = Bond(
    name='Convertible Bond', annual_return=0.05, 
    risk=0.1, issued_institution='Bank of America', market='NYSE'
    )
    
callable_bond = Bond(
    name='Callable Bond', annual_return=0.05, 
    risk=0.1, issued_institution='Bank of America', market='NYSE'
    )

government_bond = Bond(
    name='Government Bond', annual_return=0.05, 
    risk=0.1, issued_institution='Bank of America', market='NYSE'
    )

zero_coupon_bond = Bond(
    name='Zero Coupon Bond', annual_return=0.05, 
    risk=0.1, issued_institution='Bank of America', market='NYSE'
    )

corporate_bond = Bond(
    name='Corporate Bond', annual_return=0.05, 
    risk=0.1, issued_institution='Bank of America', market='NYSE'
    )

commercial_loan = Loan(
    name='Commercial Loan', annual_return=0.05, 
    risk=0.1, issued_institution='Bank of America', market='NYSE'
    )

construction_loan = Loan(

)

consumer_loan = Loan(
    
    )

government_bond = GovernmentDebtInstrument(
    issuer=Polity(name="Country A"),  # Assuming Polity is a defined class
    borrower=Borrower(name="Government of Country A"),
    call_feature=[CallFeature(description="Feature A")],  # List of CallFeature instances
    interest_payment_terms=InterestPaymentTerms(terms="Fixed 5%"),
    lender=Lender(name="Lender X"),
    offering=[DebtOffering(details="Offering Details")],
    contract_party=[ContractParty(name="Party 1"), ContractParty(name="Party 2")],
    contractual_element=[ContractualElement(element="Element A")],
    creditor=Creditor(name="Creditor Y"),
    debtor=Debtor(name="Debtor Z"),
    debt_terms=DebtTerms(terms="Term Details"),
    corresponding_account=[LoanOrCreditAccount(account_id="12345")],
    maturity_date=datetime.date(2030, 1, 1),
    financial_instrument_short_name="GovBondA",
    nominal_value=1000000.0,
    securities_restriction=[SecuritiesRestriction(restriction="Restriction A")],
    financial_instrument_classifier=[FinancialInstrumentClassifier(classifier="Classifier A")],
    industry_sector_classifier=[IndustrySectorClassifier(classifier="Sector A")],
    counterparty=Counterparty(name="Counterparty B"),
    effective_date_time_stamp=datetime.datetime(2020, 1, 1, 12, 0),
    execution_date=datetime.date(2020, 1, 1),
    execution_date_time_stamp=datetime.datetime(2020, 1, 1, 12, 0),
    principal_party=ContractPrincipal(name="Principal C")
)

municipal_security = GovernmentDebtInstrument(
    issuer=Polity(name="City of Springfield"),  # An example issuer (city government)
    borrower=Borrower(name="Municipal Government"),
    call_feature=[CallFeature(description="Municipal Call Feature")],
    interest_payment_terms=InterestPaymentTerms(terms="Variable Rate"),
    lender=Lender(name="Municipal Bond Lender"),
    offering=[DebtOffering(details="Public Infrastructure Offering")],
    contract_party=[ContractParty(name="Municipality"), ContractParty(name="Investor Group")],
    contractual_element=[ContractualElement(element="Municipal Bond Terms")],
    creditor=Creditor(name="Municipal Creditor"),
    debtor=Debtor(name="Municipal Debtor"),
    debt_terms=DebtTerms(terms="Municipal Debt Terms"),
    corresponding_account=[LoanOrCreditAccount(account_id="98765")],
    maturity_date=datetime.date(2040, 1, 1),
    financial_instrument_short_name="MuniSecurity2020",
    nominal_value=500000.0,
    securities_restriction=[SecuritiesRestriction(restriction="Municipal Restriction")],
    financial_instrument_classifier=[FinancialInstrumentClassifier(classifier="Municipal Bonds")],
    industry_sector_classifier=[IndustrySectorClassifier(classifier="Public Infrastructure")],
    counterparty=Counterparty(name="Infrastructure Investor"),
    effective_date_time_stamp=datetime.datetime(2020, 6, 1, 9, 0),
    execution_date=datetime.date(2020, 6, 1),
    execution_date_time_stamp=datetime.datetime(2020, 6, 1, 9, 0),
    principal_party=ContractPrincipal(name="Municipal Principal")
)


sovereign_debt_instrument = GovernmentDebtInstrument(
    issuer=Polity(name="Country B"),  # An example issuer (national government)
    borrower=Borrower(name="Government of Country B"),
    call_feature=[CallFeature(description="Sovereign Call Feature")],
    interest_payment_terms=InterestPaymentTerms(terms="Fixed 4%"),
    lender=Lender(name="International Finance Corporation"),
    offering=[DebtOffering(details="National Infrastructure Development")],
    contract_party=[ContractParty(name="National Government"), ContractParty(name="Global Investors")],
    contractual_element=[ContractualElement(element="Sovereign Loan Agreement")],
    creditor=Creditor(name="Sovereign Creditor"),
    debtor=Debtor(name="Sovereign Debtor"),
    debt_terms=DebtTerms(terms="Sovereign Debt Terms"),
    corresponding_account=[LoanOrCreditAccount(account_id="123456789")],
    maturity_date=datetime.date(2050, 12, 31),
    financial_instrument_short_name="SovDebt2020",
    nominal_value=100000000.0,
    securities_restriction=[SecuritiesRestriction(restriction="International Trade Restriction")],
    financial_instrument_classifier=[FinancialInstrumentClassifier(classifier="Sovereign Debt")],
    industry_sector_classifier=[IndustrySectorClassifier(classifier="National Infrastructure")],
    counterparty=Counterparty(name="International Investor"),
   

apple_common_stock = CommonStock(
    financial_instrument_short_name="AAPL",
    nominal_value=145.30,  # Example share price
    securities_restriction=[],
    financial_instrument_classifier=[],
    industry_sector_classifier=[],
    contract_party=[],
    contractual_element=[],
    effective_date=datetime.date(2022, 1, 1),
    counterparty=None,
    effective_date_time_stamp=datetime.datetime(2022, 1, 1, 9, 0),
    execution_date=datetime.date(2022, 1, 1),
    execution_date_time_stamp=datetime.datetime(2022, 1, 1, 9, 0),
    principal_party=None,
    floating_shares=10000000,  # Hypothetical number of floating shares
    share_class="Class A",
    share_payment_status="Fully Paid",
    shares_authorized=5000000000,  # Hypothetical authorized shares
    enhanced_voting_rights=False,
    restricted=False,
    fully_paid=True,
    nil_paid=False,
    partly_paid=False,
    unrestricted=True
)

tesla_preferred_stock = PreferredStock(
    financial_instrument_short_name="TSLA-P",
    nominal_value=730.00,  # Example share price for preferred stock
    securities_restriction=[],
    financial_instrument_classifier=[],
    industry_sector_classifier=[],
    contract_party=[],
    contractual_element=[],
    effective_date=datetime.date(2022, 2, 1),
    counterparty=None,
    effective_date_time_stamp=datetime.datetime(2022, 2, 1, 10, 0),
    execution_date=datetime.date(2022, 2, 1),
    execution_date_time_stamp=datetime.datetime(2022, 2, 1, 10, 0),
    principal_party=None,
    floating_shares=500000,  # Hypothetical number of floating shares for preferred stock
    share_class="Preferred",
    share_payment_status="Partly Paid",
    shares_authorized=1000000,  # Hypothetical authorized preferred shares
    convertible=True,
    cumulative=True,
    exchangeable=False,
    extendable=False,
    non_cumulative=False,
    is_senior_to_common_share=True,
    dividend=0.05  # Hypothetical dividend rate
)

amazon_restricted_share = RestrictedShare(
    financial_instrument_short_name="AMZN-R",
    nominal_value=3300.00,  # Example share price for restricted stock
    securities_restriction=[],
    financial_instrument_classifier=[],
    industry_sector_classifier=[],
    contract_party=[],
    contractual_element=[],
    effective_date=datetime.date(2022, 3, 1),
    counterparty=None,
    effective_date_time_stamp=datetime.datetime(2022, 3, 1, 11, 0),
    execution_date=datetime.date(2022, 3, 1),
    execution_date_time_stamp=datetime.datetime(2022, 3, 1, 11, 0),
    principal_party=None,
    floating_shares=200000,  # Hypothetical number of floating restricted shares
    share_class="Restricted",
    share_payment_status="Fully Paid",
    shares_authorized=500000,  # Hypothetical authorized restricted shares
    enhanced_voting=False,
    non_voting=True,
    fully_paid=True,
    nil_paid=False,
    partly_paid=False,
    unrestricted=False
)

forward_instance = Forward(
    financial_instrument_short_name="ForwardExample",
    nominal_value=100000,  # Example nominal value
    derivative_terms=DerivativeTerms(terms="Specific Terms for Forward"),
    settlement_terms=SettlementTerms(terms="Settlement Terms"),
    underlier=Underlier(asset="Commodity or Financial Asset"),
    valuation_terms=ValuationTerms(terms="Valuation Method"),
    contract_party=[ContractParty("Party A"), ContractParty("Party B")],
    contractual_element=[ContractualElement("Contractual Element for Forward")],
    effective_date=datetime.date(2023, 1, 1),
    counterparty=Counterparty("Counterparty Name"),
    effective_date_time_stamp=datetime.datetime(2023, 1, 1, 9, 0),
    execution_date=datetime.date(2023, 1, 1),
    execution_date_time_stamp=datetime.datetime(2023, 1, 1, 9, 0),
    principal_party=ContractPrincipal("Principal Party Name")
)

option_instance = Option(
    financial_instrument_short_name="OptionExample",
    nominal_value=50000,  # Example nominal value
    derivative_terms=DerivativeTerms(terms="Specific Terms for Option"),
    settlement_terms=SettlementTerms(terms="Settlement Terms"),
    underlier=Underlier(asset="Stock or Index"),
    valuation_terms=ValuationTerms(terms="Valuation Method"),
    contract_party=[ContractParty("Party C"), ContractParty("Party D")],
    contractual_element=[ContractualElement("Contractual Element for Option")],
    effective_date=datetime.date(2023, 2, 1),
    counterparty=Counterparty("Counterparty Name"),
    effective_date_time_stamp=datetime.datetime(2023, 2, 1, 10, 0),
    execution_date=datetime.date(2023, 2, 1),
    execution_date_time_stamp=datetime.datetime(2023, 2, 1, 10, 0),
    principal_party=ContractPrincipal("Principal Party Name"),
    lot_size=100  # Example lot size
)

future_instance = Future(
    financial_instrument_short_name="FutureExample",
    nominal_value=200000,  # Example nominal value
    derivative_terms=DerivativeTerms(terms="Specific Terms for Future"),
    settlement_terms=SettlementTerms(terms="Settlement Terms"),
    underlier=Underlier(asset="Energy or Agricultural Product"),
    valuation_terms=ValuationTerms(terms="Valuation Method"),
    contract_party=[ContractParty("Party E"), ContractParty("Party F")],
    contractual_element=[ContractualElement("Contractual Element for Future")],
    effective_date=datetime.date(2023, 3, 1),
    counterparty=Counterparty("Counterparty Name"),
    effective_date_time_stamp=datetime.datetime(2023, 3, 1, 11, 0),
    execution_date=datetime.date(2023, 3, 1),
    execution_date_time_stamp=datetime.datetime(2023, 3, 1, 11, 0),
    principal_party=ContractPrincipal("Principal Party Name"),
    settlement_date=datetime.date(2023, 12, 1),  # Example settlement date
    contract_size=500,  # Example contract size
    tick_size=0.05  # Example tick size
)
