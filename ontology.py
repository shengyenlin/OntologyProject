from dataclasses import dataclass

@dataclass
class JudicialEntity:
    pass


@dataclass
class FinancialInstruments:
    # properties
    annual_return: float
    market: JudicialEntity

@dataclass
class FinancialMarketParticipants(JudicialEntity):
    pass

@dataclass
class SecutityCompany():
    pass

@dataclass
class DebtInstrument(FinancialInstruments):
    # properties
    interest_rate: float
    issuer: SecutityCompany
    market: FinancialMarketParticipants




bond = DebtInstrument(annual_return=0.05, interest_rate=0.05, issuer="Bank")
