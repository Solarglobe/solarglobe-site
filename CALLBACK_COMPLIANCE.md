# Conformité des demandes de rappel SolarGlobe

Date : 26/08/2026

Ce dépôt contient le site public statique. Il ne contient pas le CRM d’appel ni le backend de scoring des prospects achetés. Les formulaires publics transmettent une preuve minimale horodatable, mais cette preuve reste constituée côté navigateur puis envoyée via FormSubmit. Elle ne remplace donc pas une preuve serveur robuste : le `request_id`, le calcul des cinq jours ouvrables, le stockage de l’instantané, le hash de preuve, les statuts d’appel et le blocage opérationnel doivent être recalculés, validés et conservés côté serveur ou dans le CRM qui consomme ces demandes.

## Payload minimal attendu

- request_id
- lead_id
- consumer_name
- phone_number
- request_timestamp
- source_type
- source_url
- form_version
- exact_request_text
- requested_services
- callback_deadline
- evidence_status
- partner_name
- partner_evidence_id
- proof_file_or_snapshot
- proof_hash
- withdrawn_at
- do_not_call
- created_at
- updated_at

## Texte exact de demande de rappel

Je demande expressément à SolarGlobe de me rappeler au sujet de mon projet photovoltaïque et des services que j’ai sélectionnés.

## Statuts CRM requis

- callback_request_valid
- existing_contract
- proof_missing
- expired
- withdrawn
- do_not_call
- legal_review_required

## Règles d’appel

`callback_deadline = demande + 5 jours ouvrables`, fuseau Europe/Paris. Le samedi compte comme jour ouvrable, le dimanche et les jours fériés habituellement non travaillés ne comptent pas. Le calcul commence le jour ouvrable suivant la demande.

Téléphone bloqué si statut : `proof_missing`, `expired`, `withdrawn`, `do_not_call`, `legal_review_required`. Tout déblocage manuel doit être journalisé avec utilisateur, date, justification et preuve.

Les champs cachés transmis par le site ne doivent pas être considérés comme une source d’autorisation suffisante à eux seuls. Le CRM doit vérifier ou reconstruire la preuve à partir d’un enregistrement serveur, puis bloquer par défaut tout prospect dont la preuve est absente, expirée, retirée, ambiguë ou non rattachée explicitement à SolarGlobe.

## Prospects achetés

Un fichier contenant seulement nom, téléphone et opt-in oui ne suffit pas. Si SolarGlobe n’est pas clairement identifiable dans la preuve, classer le prospect en `legal_review_required`. Les anciens prospects sans preuve exploitable doivent rester `proof_missing`.
